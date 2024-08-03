
from code.layer1 import layer1

# obj = layer1()
# ret = obj._flow(inps=[
#     {
#         "single_int": {
#             "inp_int": 10
#         }
#     },
#     {
#         "single_float": {
#             "inp_float": 10.0
#         }
#     },
#     {
#         "l2": [
#             {
#                 "single_int": {
#                     "inp_int": 10
#                 }
#             },
#             {
#                 "single_float": {
#                     "inp_float": 10.0
#                 }
#             }
#         ],
#     }
# ], meta={
#     "func": None,
#     "path": obj.__class__.__name__
# })
# print(ret)

# obj = layer1()
# ret = obj._flow(inps=[
#     {
#         "single_int": {
#             "inp_int": 10
#         }
#     },
#     {
#         "single_float": {
#             "inp_float": 10.0
#         }
#     },
#     {
#         "l2": "conf/l2.json",
#     }
# ], meta={
#     "func": None,
#     "path": obj.__class__.__name__
# })
# print(ret)

import json
import pathlib

obj = layer1()
ret = obj._flow(inps=pathlib.Path("conf/l1.json"), meta={
    "func": None,
    "path": obj.__class__.__name__
})
print(json.dumps(ret, indent=2, sort_keys=True))