
from py4mbd.outer import node
from code.layer1 import layer1

import json

Node = node(layer1)

# DOCS API

docs = Node._docs(obj_path="layer1", incs=[])
print(">>>", "layer1")
print(json.dumps(docs, indent=2, sort_keys=True))

docs = Node._docs(obj_path="layer1/dummy", incs=[])
print(">>>", "layer1/dummy")
print(json.dumps(docs, indent=2, sort_keys=True))

docs = Node._docs(obj_path="layer1/l2", incs=[])
print(">>>", "layer1/l2")
print(json.dumps(docs, indent=2, sort_keys=True))

docs = Node._docs(obj_path="layer1/l2/dummy", incs=[])
print(">>>", "layer1/l2/dummy")
print(json.dumps(docs, indent=2, sort_keys=True))

docs = Node._docs(obj_path="layer1/l2/l3", incs=[])
print(">>>", "layer1/l2/l3")
print(json.dumps(docs, indent=2, sort_keys=True))

docs = Node._docs(obj_path="layer1/l2/l3/dummy", incs=[])
print(">>>", "layer1/l2/l3/dummy")
print(json.dumps(docs, indent=2, sort_keys=True))

docs = Node._docs(obj_path="layer1/l2/l3/summa", incs=[])
print(">>>", "layer1/l2/l3/summa")
print(json.dumps(docs, indent=2, sort_keys=True))

docs = Node._docs(obj_path="layer1/l2/l3/l4", incs=[])
print(">>>", "layer1/l2/l3/l4")
print(json.dumps(docs, indent=2, sort_keys=True))

docs = Node._docs(obj_path="layer1/l2/l3/l4/dummy", incs=[])
print(">>>", "layer1/l2/l3/l4/dummy")
print(json.dumps(docs, indent=2, sort_keys=True))

docs = Node._docs(obj_path="layer1/l4", incs=[])
print(">>>", "layer1/l4")
print(json.dumps(docs, indent=2, sort_keys=True))

docs = Node._docs(obj_path="layer1/l4/dummy", incs=[])
print(">>>", "layer1/l4/dummy")
print(json.dumps(docs, indent=2, sort_keys=True))
