from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Setup the Jinja2 template directory
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    # Render the main calculator page
    return templates.TemplateResponse("index.html", {"request": request, "result": None})

@app.post("/calculate", response_class=HTMLResponse)
async def calculate(
    request: Request,
    operation: str = Form(...),
    a: float = Form(...),
    b: float = Form(...),
):
    # Validate the operation
    if operation not in ["add", "subtract", "multiply", "divide"]:
        raise HTTPException(status_code=400, detail="Invalid operation.")
    
    # Perform the calculation
    try:
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
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    # Return the result without redirecting
    return templates.TemplateResponse("index.html", {
        "request": request,
        "result": result,
        "a": a,
        "b": b,
        "operation": operation
    })

