from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import pipe
import asyncio

app = FastAPI()

@app.post("/hello/{name}")
async def hello_endpoint(name: str):
    # index_note is async, so it will return before its execution.
    # If it fails for some reason, the client won't know.
    asyncio.create_task(pipe.index_note(name))

    response_body = {"message": f"Hello, {name}!"}
    return JSONResponse(content=response_body, status_code=201)
