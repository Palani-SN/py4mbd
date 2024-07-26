
import pathlib
import inspect
from typing import Union
from copy import deepcopy

# DEV mode with hot reload via api server
# REL mode with preprocessing in Init for Later Validation 
class pod:

    # always read only (DEV & REL)
    def _docs(self, meta: dict = {}) -> dict:

        # meta manipulation
        # mode : ( DEV / REL as <Str>)
        # include : ( Any of [desc, params, docs, kwargs, ret] as <List> )
        # xpath : ( xpath or ignore )
        # meta_mode = meta['mode'] if 'mode' in meta.keys() else 'DEV'
        meta_inc = meta['inc'] if 'inc' in meta.keys() else ['desc', 'params', 'docs', 'kwargs', 'ret']
        meta_path = meta['key'] if 'key' in meta.keys() else self.__class__.__name__

        # inspect classes & functions
        # make recursive docs calls to fetch documentation of all functions in all sub objects
        methods = []
        classes = []
        for name, obj in inspect.getmembers(self):
            func_path = f"{meta_path}/{name}"
            if not meta['func'] or func_path == meta['func']:
                if not name.startswith('_') and inspect.ismethod(obj):

                    # Preparing Desc
                    desc = None
                    raw_desc = inspect.getcomments(obj)
                    if raw_desc:
                        desc = [ x.strip(' # ') for x in raw_desc.splitlines()]
                    # ===

                    # Preparing docs
                    docs = None
                    raw_docs = inspect.getdoc(obj)
                    if raw_docs:
                        docs = [ x.rstrip() for x in raw_docs.splitlines()]
                    # ===

                    # ---
                    sign = inspect.signature(obj)

                    # Preparing Params
                    params = [str(val) for var, val in sign.parameters.items()]
                    # ===

                    # Preparing Kwargs
                    kwargs = {}
                    for key, val in sign.parameters.items():
                        if val.default == inspect._empty:
                            kwargs[key] = {
                                'value': val.default,
                                'type': val.annotation.__name__}
                        else:
                            kwargs[key] = {
                                'value': val.default,
                                'type': val.annotation.__name__
                                }
                    # ===

                    # Preparing return type
                    ret = sign.return_annotation.__name__
                    # ==

                    # ---
                    # Preparing payload
                    payload = {
                        'type': 'func',
                        'key': func_path,
                        'label': name
                        }
                    for key in meta_inc:
                        payload[key] = locals() [key]
                    # ===
                    methods.append(payload)

        mod_meta = deepcopy(meta)
        for name, obj in inspect.getmembers(self):
            if not meta['func']:
                if not name.startswith('_') and isinstance(obj, pod):
                    # Preparing meta
                    mod_meta.update({'key': f"{meta_path}/{name}"})
                    classes.append(getattr(self, name)._docs(meta=mod_meta))
                # ===

        class_meta = {}
        if not meta['func']:
            label = meta['key'].rsplit('/', 1)[-1]
            class_meta = {'type': 'obj', 'key': meta['key'], 'label': label, 'children': methods+classes}
        else:
            class_meta = methods[0]
        results = class_meta
        return results

    # Validate conf with code (DEV & REL) - return
    def _conf(self, inps: Union[list[dict] | pathlib.Path], meta: dict = {}) -> dict:

        meta_path = meta['path'] if 'path' in meta.keys() else self.__class__.__name__

        def chk_func(name:str, func: callable, params: dict):

            warnings = []
            ref = inspect.signature(func).parameters
            expected = set(list(ref.keys()))
            actual = set(list(params.keys()))
            if not (actual == expected):
                warnings.append(f"Expected {expected} kwargs, got {actual} kwargs instead")
            else:
                for key, val in ref.items():
                    if not val.annotation in [str, int, float, list, dict, bool, inspect._empty]:
                        warnings.append(f"Unsupported {key} : {val.annotation.__name__}, try using basic types (int, float, str, list, dict, bool) instead")
                    if not((val.annotation == inspect._empty) or (type(params[key]) == val.annotation)):
                        warnings.append(f"Expected {key} : {val.annotation.__name__}, got {key} : {type(params[key]).__name__} = {params[key]} instead")

            return warnings

        ref_methods = { x : y for x, y in inspect.getmembers(self) if not x.startswith('_') and inspect.ismethod(y) } 
        ref_classes = { x : y for x, y in inspect.getmembers(self) if not x.startswith('_') and isinstance(y, pod) }

        act_conf = []
        mod_meta = deepcopy(meta)
        for i in range(len(inps)):
            # Preparing Elements
            conf = inps[i]
            for name, params in conf.items():
                # Preparing Functions
                if name in ref_methods.keys():
                    func_path = f"{meta_path}/{name}"
                    if not meta['func'] or func_path == meta['func']:
                        func = ref_methods[name]
                        act_conf.append({'type': 'func', 'title': name, 'key': func_path, 'warnings': chk_func(name, func, params)})
                # ===

                # Preparing Classes
                if name in ref_classes.keys():
                    class_path = f"{meta_path}/{name}"
                    mod_meta.update({'path': class_path})
                    act_conf.append(getattr(self, name)._conf(inps=params, meta=mod_meta))
                # ===

        if not meta['func']:
            results = {'children': act_conf, 'type': 'obj', 'title': meta['path'].rsplit('/', 1)[-1], 'key': meta['path']}
        else:
            results = act_conf[0]
        return results

    # Executes conf on code (DEV & REL) - 
    def _exec(self, inps: Union[list[dict] | pathlib.Path], meta: dict = {}) -> dict:

        # if meta.mode == 'DEV':
        # executes conf on code without telemetry
        # if meta.mode == 'REL':
        # executes conf on code with telemetry
        meta_path = meta['path'] if 'path' in meta.keys() else self.__class__.__name__

        def run_func(name:str, func: callable, params: dict):

            warnings = []
            ref = inspect.signature(func).parameters
            expected = set(list(ref.keys()))
            actual = set(list(params.keys()))
            if not (actual == expected):
                warnings.append(f"Expected {expected} kwargs, got {actual} kwargs instead")
            else:
                for key, val in ref.items():
                    if not val.annotation in [str, int, float, list, dict, bool, inspect._empty]:
                        warnings.append(f"Unsupported {key} : {val.annotation.__name__}, try using basic types (int, float, str, list, dict, bool) instead")
                    if not((val.annotation == inspect._empty) or (type(params[key]) == val.annotation)):
                        warnings.append(f"Expected {key} : {val.annotation.__name__}, got {key} : {type(params[key]).__name__} = {params[key]} instead")

            if warnings == []:
                try:
                    return {'returned': func(*[], **params)}
                except Exception as err:
                    return {'error': str(err)}
            else:
                return {'warnings': warnings}

        ref_methods = { x : y for x, y in inspect.getmembers(self) if not x.startswith('_') and inspect.ismethod(y) } 
        ref_classes = { x : y for x, y in inspect.getmembers(self) if not x.startswith('_') and isinstance(y, pod) }

        act_conf = []
        mod_meta = deepcopy(meta)
        for i in range(len(inps)):
            # Preparing Elements
            conf = inps[i]
            for name, params in conf.items():
                # Preparing Functions
                if name in ref_methods.keys():
                    func_path = f"{meta_path}/{name}" 
                    if not meta['func'] or func_path == meta['func']:
                        func = ref_methods[name]
                        act_conf.append({'type': 'func', 'title': name, 'key': func_path, **run_func(name, func, params)})
                # ===

                # Preparing Classes
                if name in ref_classes.keys():
                    class_path = f"{meta_path}/{name}"
                    mod_meta.update({'path': class_path})
                    act_conf.append(getattr(self, name)._exec(inps=params, meta=mod_meta))
                # ===

        if not meta['func']:
            results = {'children': act_conf, 'type': 'obj', 'title': meta['path'].rsplit('/', 1)[-1], 'key': meta['path']}
        else:
            results = act_conf[0]
        return results