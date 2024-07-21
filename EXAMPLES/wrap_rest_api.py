
import time
import uvicorn
from fastapi import FastAPI

from py4mbd.outer import node

from code.layer1 import layer1

Node = node(layer1)

app = FastAPI()

@app.get("/index")
async def root():
    ret = Node._index()
    return ret

@app.post("/docs/{obj_path:path}")
async def get_docs(obj_path:str, inc: list[str]):
    return Node._docs(obj_path, inc)

@app.post("/conf/{obj_path:path}")
async def chk_conf(obj_path:str, inps: list[dict]):
    return Node._conf(obj_path, inps)

@app.post("/exec/{obj_path:path}")
async def run_exec(obj_path:str, inps: list[dict]):
    return Node._exec(obj_path, inps)

if __name__ == "__main__":
    uvicorn.run("wrap_rest_api:app", host="localhost", port=8000, reload=True)