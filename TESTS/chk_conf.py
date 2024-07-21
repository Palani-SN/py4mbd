
from py4mbd.outer import node
from code.layer1 import layer1

import json

Node = node(layer1)

# CONF API

inps = [
    {
        "dummy": {
            "inp1": "Hello [0][0]",
            "inp2": "Hello [0][1]"
        }
    },
    {
        "l2": [
            {
                "dummy": {
                    "inp1": "Hello [1][0]",
                    "inp2": "Hello [1][1]"
                }
            },
            {
                "l3": [
                    {
                        "dummy": {
                            "inp1": "Hello [1][1][0]",
                            "inp2": "Hello [1][1][1]"
                        }
                    },
                    {
                        "l4": [
                            {
                                "dummy": {
                                    "inp1": "Hello [1][1][1][0]",
                                    "inp2": "Hello [1][1][1][1]"
                                }
                            }
                        ]
                    }
                ]
            },
            {
                "l3": [
                    {
                        "dummy": {
                            "inp1": "Hello [1][2][0]",
                            "inp2": "Hello [1][2][1]"
                        }
                    },
                    {
                        "l4": [
                            {
                                "dummy": {
                                    "inp1": "Hello [1][2][1][0]",
                                    "inp2": "Hello [1][2][1][1]"
                                }
                            }
                        ]
                    }
                ]
            }
        ]
    },
    {
        "dummy": {
            "inp1": "Hello [1][0]",
            "inp2": "Hello [1][1]"
        }
    },
    {
        "l3": [
            {
                "dummy": {
                    "inp1": "Hello [2][0][0]",
                    "inp2": "Hello [2][0][1]"
                }
            },
            {
                "dummy": {
                    "inp1": "Hello [2][1][0]",
                    "inp2": "Hello [2][1][1]"
                }
            }
        ]
    },
    {
        "l4": [
            {
                "dummy": {
                    "inp1": "Hello [3][0][0]",
                    "inp2": "Hello [3][0][1]"
                }
            }
        ]
    }
]
docs = Node._conf(obj_path="layer1", inps=inps)
print(">>>", "layer1")
print(json.dumps(docs, indent=2, sort_keys=True))

inps = [
    {
        "dummy": {
            "inp1": "Hello [0][0]",
            "inp2": "Hello [0][1]"
        }
    }
]
docs = Node._conf(obj_path="layer1/dummy", inps=inps)
print(">>>", "layer1/dummy")
print(json.dumps(docs, indent=2, sort_keys=True))

inps = [
            {
                "dummy": {
                    "inp1": "Hello [1][0]",
                    "inp2": "Hello [1][1]"
                }
            },
            {
                "l3": [
                    {
                        "dummy": {
                            "inp1": "Hello [1][1][0]",
                            "inp2": "Hello [1][1][1]"
                        }
                    },
                    {
                        "l4": [
                            {
                                "dummy": {
                                    "inp1": "Hello [1][1][1][0]",
                                    "inp2": "Hello [1][1][1][1]"
                                }
                            }
                        ]
                    }
                ]
            },
            {
                "l3": [
                    {
                        "dummy": {
                            "inp1": "Hello [1][2][0]",
                            "inp2": "Hello [1][2][1]"
                        }
                    },
                    {
                        "l4": [
                            {
                                "dummy": {
                                    "inp1": "Hello [1][2][1][0]",
                                    "inp2": "Hello [1][2][1][1]"
                                }
                            }
                        ]
                    }
                ]
            }
        ]
docs = Node._conf(obj_path="layer1/l2", inps=inps)
print(">>>", "layer1/l2")
print(json.dumps(docs, indent=2, sort_keys=True))

inps = [
    {
        "dummy": {
            "inp1": "Hello [1][0]",
            "inp2": "Hello [1][1]"
        }
    }
]
docs = Node._conf(obj_path="layer1/l2/dummy", inps=inps)
print(">>>", "layer1/l2/dummy")
print(json.dumps(docs, indent=2, sort_keys=True))

inps = [
    {
        "dummy": {
            "inp1": "Hello [1][1][0]",
            "inp2": "Hello [1][1][1]"
        }
    },
    {
        "l4": [
            {
                "dummy": {
                    "inp1": "Hello [1][1][1][0]",
                    "inp2": "Hello [1][1][1][1]"
                }
            }
        ]
    }
]
docs = Node._conf(obj_path="layer1/l2/l3", inps=inps)
print(">>>", "layer1/l2/l3")
print(json.dumps(docs, indent=2, sort_keys=True))

inps = [
    {
        "dummy": {
            "inp1": "Hello [1][1][0]",
            "inp2": "Hello [1][1][1]"
        }
    }
]
docs = Node._conf(obj_path="layer1/l2/l3/dummy", inps=inps)
print(">>>", "layer1/l2/l3/dummy")
print(json.dumps(docs, indent=2, sort_keys=True))

inps = [
    {
        "summa": {
            "inp1": "Hello [1][1][0]",
            "inp2": "Hello [1][1][1]"
        }
    }
]
docs = Node._conf(obj_path="layer1/l2/l3/summa", inps=inps)
print(">>>", "layer1/l2/l3/summa")
print(json.dumps(docs, indent=2, sort_keys=True))

inps = [
    {
        "dummy": {
            "inp1": "Hello [1][1][1][0]",
            "inp2": "Hello [1][1][1][1]"
        }
    }
]
docs = Node._conf(obj_path="layer1/l2/l3/l4", inps=inps)
print(">>>", "layer1/l2/l3/l4")
print(json.dumps(docs, indent=2, sort_keys=True))

inps = [
    {
        "dummy": {
            "inp1": "Hello [1][1][1][0]",
            "inp2": "Hello [1][1][1][1]"
        }
    }
]
docs = Node._conf(obj_path="layer1/l2/l3/l4/dummy", inps=inps)
print(">>>", "layer1/l2/l3/l4/dummy")
print(json.dumps(docs, indent=2, sort_keys=True))

inps = [
    {
        "dummy": {
            "inp1": "Hello [1][1][1][0]",
            "inp2": "Hello [1][1][1][1]"
        }
    }
]
docs = Node._conf(obj_path="layer1/l4", inps=inps)
print(">>>", "layer1/l4")
print(json.dumps(docs, indent=2, sort_keys=True))

inps = [
    {
        "dummy": {
            "inp1": "Hello [1][1][1][0]",
            "inp2": "Hello [1][1][1][1]"
        }
    }
]
docs = Node._conf(obj_path="layer1/l4/dummy", inps=inps)
print(">>>", "layer1/l4/dummy")
print(json.dumps(docs, indent=2, sort_keys=True))