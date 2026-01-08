from flask import Flask, request, jsonify
from .task_service import create_task, get_tasks



app = Flask(__name__)

@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.json
    task = create_task(
        title=data["title"],
        priority=data.get("priority", "Normal")
    )
    return jsonify(task), 201

@app.route("/tasks", methods=["GET"])
def list_tasks():
    return jsonify(get_tasks())

if __name__ == "__main__":
    app.run()

