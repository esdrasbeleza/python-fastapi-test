# Playing with FastAPI & unit tests

## Run the server:

1. `uvicorn main:app --reload`
2. Run `curl -X POST localhost:8000/hello/esdras`

This endpoint will answer the call immediatelly, but it will call `pipe.index_note`, which will take 10 seconds to answer.

## Run the tests

Just run `pytest`.

The test we have will not call the real `pipe.index_note`, but a mock.
