from flask import Flask, request, jsonify

app = Flask(__name__)

data = {
    "name": "Aniket",
    "company": "Ajinkyaaa Bari",
    "message": "Hello from Docker Agent 🚀"
}


@app.route("/")
def home():
    return jsonify(data)


@app.route("/update", methods=["POST"])
def update_data():
    new_data = request.get_json()

    if not new_data:
        return jsonify({"error": "No data provided"}), 400

    data.update(new_data)

    return jsonify({
        "message": "Data updated successfully",
        "data": data
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

