
import re
# import json
from py4mbd.inner import pod
from datetime import datetime

# from functools import reduce  # forward compatibility for Python 3
# import operator

class node:

    pods = {}

    def __init__(self, root: pod) -> None:
        
        self.pods[root().__class__.__name__] = root

    def _index(self):

        ret = {
        "py4mbd": "online", 
        "root": list(self.pods.keys()),
        "time": datetime.now().isoformat()
        }
        return ret

    # always read only (DEV & REL)
    def _docs(self, obj_path:str, incs: list[str]) -> dict:

        def params(obj_path, include):

            inc_set = set(include)
            exp_set = set(["kwargs","desc", "params", "docs","ret"])
            inc_ok = inc_set <= exp_set if inc_set else True
            if not inc_ok:
                Exception(f"Expected subset of ['kwargs','desc', 'params', 'docs','ret'], got {include} instead")

            splitted = re.split('/', obj_path)
            root, leaf = splitted[0], splitted[-1]

            if not root in self.pods.keys():
                raise Exception(f"Cannot Find {root}, try using any of {list(self.pods.keys())} instead")

            locals()[root] = self.pods[root]()
            obj = eval('.'.join(splitted))
            if isinstance(obj, pod):
                return obj, obj_path, None, include
            obj = eval('.'.join(splitted[:-1]))
            if isinstance(obj, pod):
                return obj, '/'.join(splitted[:-1]), obj_path, include

        try:
            root, prefix, func, inc = params(obj_path, incs)

            # Actual Call to the Code
            result = root._docs(meta={
                'inc': inc,
                'key': prefix,
                'func': func
            })

            # ===
            # print(json.dumps(result, indent=2))
            # ===
        except (Exception) as err:
            result = {'error': str(err)}
        return {obj_path: result, 'time': datetime.now().isoformat()}

    # Validate conf with code (DEV & REL) - return
    def _conf(self, obj_path:str, inps: list[dict]) -> dict:

        def params(obj_path, inputs):

            if type(inputs) != list:
                raise Exception(f"Inputs has to be of type list[dict], got {type(inputs)} instead")

            splitted = re.split('/', obj_path)
            root, leaf = splitted[0], splitted[-1]

            if not root in self.pods.keys():
                raise Exception(f"Cannot Find {root}, try using any of {list(self.pods.keys())} instead")

            locals()[root] = self.pods[root]()
            obj = eval('.'.join(splitted))
            if isinstance(obj, pod):
                return obj, obj_path, None, inputs
            obj = eval('.'.join(splitted[:-1]))
            if isinstance(obj, pod):
                return obj, '/'.join(splitted[:-1]), obj_path, inputs

        try:
            root, prefix, func, inps = params(obj_path, inps)

            # Actual Call to the Code
            result = root._conf(meta={
                'path': prefix,
                'func': func
            }, inps=inps)

            # ===
            # print(json.dumps(result, indent=2))
            # ===
        except (Exception) as err:
            result = {'error': str(err)}
        return {obj_path: result, 'time': datetime.now().isoformat()}

    # Executes conf on code (DEV & REL) - 
    def _exec(self, obj_path:str, inps: list[dict]) -> dict:

        # if meta.mode == 'DEV':
        # executes conf on code without telemetry
        # if meta.mode == 'REL':
        # executes conf on code with telemetry
        def params(obj_path, inputs):

            if type(inputs) != list:
                raise Exception(f"Inputs has to be of type list[dict], got {type(inputs)} instead")

            splitted = re.split('/', obj_path)
            root, leaf = splitted[0], splitted[-1]

            if not root in self.pods.keys():
                raise Exception(f"Cannot Find {root}, try using any of {list(self.pods.keys())} instead")

            locals()[root] = self.pods[root]()
            obj = eval('.'.join(splitted))
            if isinstance(obj, pod):
                return obj, obj_path, None, inputs
            obj = eval('.'.join(splitted[:-1]))
            if isinstance(obj, pod):
                return obj, '/'.join(splitted[:-1]), obj_path, inputs

        try:
            root, prefix, func, inps = params(obj_path, inps)

            # Actual Call to the Code
            result = root._exec(meta={
                'path': prefix,
                'func': func
            }, inps=inps)

            # ===
            # print(json.dumps(result, indent=2))
            # ===
        except (Exception) as err:
            result = {'error': str(err)}
        return {obj_path: result, 'time': datetime.now().isoformat()}