from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class CalculationRequest(BaseModel):
    a: float
    b: float
    operation: str

@app.post("/calc")
def calculate(data: CalculationRequest):
    a, b, operation = data.a, data.b, data.operation
    if operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b
    elif operation == "multiply":
        result = a * b
    elif operation == "divide":
        if b == 0:
            raise HTTPException(status_code=400, detail="Cannot divide by zero")
        result = a / b
    else:
        raise HTTPException(status_code=400, detail="Invalid operation")
    return {"operation": operation, "a": a, "b": b, "result": result}
