from fastapi.testclient import TestClient
from unittest.mock import patch
import time
import asyncio
from main import app

client = TestClient(app)

@patch('main.pipe.index_note')  # Patch the module path to pipe.index_note
def test_hello_endpoint(mock_index_note):
    # Configure the mock behavior to sleep for 3 seconds
    async def mocked_index_note(name):
        await asyncio.sleep(3)
        print("This function will run on background, and this call will be reached after 3s")

    # Notice that even though we're not calling the real index_note,
    # it will still be executed async'ly
    mock_index_note.side_effect = mocked_index_note

    start_time = time.time()
    response = client.post("/hello/Esdras")
    end_time = time.time()

    # Assert the response
    assert response.status_code == 201
    assert response.json() == {"message": "Hello, Esdras!"}

    # Assert that the mocked function was called with the correct argument
    mock_index_note.assert_called_once_with("Esdras")

    # Assert that the elapsed time is less than 1 second
    elapsed_time = end_time - start_time
    assert elapsed_time < 1.0
