import time

# index_note is async, so it will return before its execution
async def index_note(name: str):
    print("starting indexing " + name)
    time.sleep(10)
    print("indexing finished")
