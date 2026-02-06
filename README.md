# Calculator Service

A simple FastAPI-based calculator microservice with add, subtract, multiply, and divide endpoints.

## Running the Service

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## API Endpoints
- `/calculator/add?a=2&b=3`
- `/calculator/subtract?a=5&b=2`
- `/calculator/multiply?a=4&b=3`
- `/calculator/divide?a=10&b=2`

## Health Check
- `/healthz`

## Running Tests

```bash
pytest
```
