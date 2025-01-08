uvicorn api_fastapi:app --reload
@REM Uvicorn is an ASGI (Asynchronous Server Gateway Interface) web server implementation for Python. https://www.uvicorn.org/

@REM check
@REM http://127.0.0.1:8000
@REM http://127.0.0.1:8000/path
@REM http://127.0.0.1:8000/path/1
@REM curl -X POST "http://localhost:8000/path" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"msg\":\"your message here\"}"
