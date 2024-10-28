from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

# Pydantic model for the calculator input
class CalculationInput(BaseModel):
    a: float
    b: float
    operation: str

@app.post("/calculate", response_class=JSONResponse)
async def calculate(data: CalculationInput):
    result = None
    if data.operation == "add":
        result = data.a + data.b
    elif data.operation == "subtract":
        result = data.a - data.b
    elif data.operation == "multiply":
        result = data.a * data.b
    elif data.operation == "divide":
        if data.b == 0:
            result = "Cannot divide by zero"
        else:
            result = data.a / data.b
    else:
        return JSONResponse(content={"error": "Invalid operation"}, status_code=400)

    return JSONResponse(content={"result": result})
