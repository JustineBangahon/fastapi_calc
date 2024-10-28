from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/calculate", response_class=HTMLResponse)
async def calculate(
    request: Request,
    operation: str = Form(...),
    a: float = Form(...),
    b: float = Form(...),
):
    # Ensure operation is one of the expected values
    if operation not in ["add", "subtract", "multiply", "divide"]:
        raise HTTPException(status_code=400, detail="Invalid operation.")
    
    # Perform the calculation
    if operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b
    elif operation == "multiply":
        result = a * b
    elif operation == "divide":
        if b == 0:
            raise HTTPException(status_code=400, detail="Division by zero is not allowed.")
        result = a / b

    # Return the result on the same page without redirecting
    return templates.TemplateResponse("index.html", {
        "request": request,
        "result": result,
        "a": a,
        "b": b,
        "operation": operation
    })

