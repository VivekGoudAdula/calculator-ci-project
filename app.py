from flask import Flask, request, jsonify
from calculator import add, subtract, multiply, divide

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>CI/CD Calculator</title>
        <style>
            body {
                background: #0f172a;
                color: white;
                font-family: Arial;
                text-align: center;
                padding: 100px 20px;
            }
            h1 { color: #38bdf8; }
            p { color: #cbd5e1; }
        </style>
    </head>
    <body>
        <h1>CI/CD Calculator Application</h1>
        <p>Successfully deployed using GitHub Actions and Render.</p>
        <p>Application Status: Running</p>
    </body>
    </html>
    """


@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()

    operation = data.get("operation")
    a = data.get("a")
    b = data.get("b")

    operations = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide
    }

    if operation not in operations:
        return jsonify({"error": "Invalid operation"}), 400

    try:
        result = operations[operation](a, b)
    except TypeError:
        return jsonify({"error": "Invalid input"}), 400

    if result == "Error":
        return jsonify({"error": "Division by zero"}), 400

    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
