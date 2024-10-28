from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse

app = FastAPI()

# HTML with embedded CSS and escaped curly braces
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Web-based Calculator</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 20px;
        }}
        form {{
            margin: 20px 0;
        }}
        label, input, select, button {{
            margin: 5px;
        }}
    </style>
</head>
<body>
    <h1>Web-based Calculator</h1>
    <form action="/calculate" method="post">
        <label for="a">First Number:</label>
        <input type="number" name="a" step="any" required>
        
        <label for="b">Second Number:</label>
        <input type="number" name="b" step="any" required>

        <label for="operation">Operation:</label>
        <select name="operation" required>
            <option value="add">Add</option>
            <option value="subtract">Subtract</option>
            <option value="multiply">Multiply</option>
            <option value="divide">Divide</option>
        </select>

        <button type="submit">Calculate</button>
    </form>
    
    {result_display}
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def calculator_form():
    # Render the calculator form without any result
    return HTMLResponse(content=html_content.format(result_display=""))

@app.post("/calculate", response_class=HTMLResponse)
async def calculate(data: dict = Body(...)):
    a = data.get('a')
    b = data.get('b')
    operation = data.get('operation')

    result = None
    if operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b
    elif operation == "multiply":
        result = a * b
    elif operation == "divide":
        if b == 0:
            result = "Cannot divide by zero"
        else:
            result = a / b

    # Render the HTML with the result displayed
    result_display = f"<h2>Result: {result}</h2>"
    return HTMLResponse(content=html_content.format(result_display=result_display))
