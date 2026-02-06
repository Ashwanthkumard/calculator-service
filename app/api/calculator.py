from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/calculator", tags=["calculator"])

@router.get("/add")
def add(a: float, b: float):
    return {"operation": "add", "result": a + b}

@router.get("/subtract")
def subtract(a: float, b: float):
    return {"operation": "subtract", "result": a - b}

@router.get("/multiply")
def multiply(a: float, b: float):
    return {"operation": "multiply", "result": a * b}

@router.get("/divide")
def divide(a: float, b: float):
    if b == 0:
        raise HTTPException(status_code=400, detail="Division by zero")
    return {"operation": "divide", "result": a / b}
