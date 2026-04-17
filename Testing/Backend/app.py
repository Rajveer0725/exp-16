from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask API is running 🚀"

@app.route("/add")
def add():
    a = request.args.get("a")
    b = request.args.get("b")

    # Check if parameters are missing
    if a is None or b is None:
        return jsonify({"error": "Parameters 'a' and 'b' are required"}), 400

    try:
        a = int(a)
        b = int(b)
        return jsonify({"result": a + b})
    except ValueError:
        return jsonify({"error": "Please provide valid integers"}), 400


if __name__ == "__main__":
    app.run(debug=True, port=5001)