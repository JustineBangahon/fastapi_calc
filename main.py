from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Calculation(BaseModel):
    operation: str
    number1: float
    number2: float

@app.post("/calculate/")
def calculate(calc: Calculation):
    if calc.operation == "add":
        result = calc.number1 + calc.number2
    elif calc.operation == "subtract":
        result = calc.number1 - calc.number2
    elif calc.operation == "multiply":
        result = calc.number1 * calc.number2
    elif calc.operation == "divide":
        if calc.number2 == 0:
            return {"error": "Cannot divide by zero"}
        result = calc.number1 / calc.number2
    else:
        return {"error": "Invalid operation"}
    
    return {"result": result}
