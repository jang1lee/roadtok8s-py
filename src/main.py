from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_index():
    """
    Return a Python dictionary with a single key-value pair.
    """
    return {"Hello": "World"}

@app.get("/api/v1/hello-world")
def read_hello_world():
    """
    Return an API-like response.
    """
    return {"what": "road", "where": "kubernetes", "version": "v1"}