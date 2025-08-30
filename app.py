from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory workout storage
workouts = []

@app.route('/')
def home():
    return jsonify({"message": "Welcome to ACEest Fitness & Gym API"})

@app.route('/add_workout', methods=['POST'])
def add_workout():
    data = request.json
    workout = data.get("workout")
    duration = data.get("duration")

    if not workout or not duration:
        return jsonify({"error": "Workout and duration required"}), 400

    try:
        duration = int(duration)
    except ValueError:
        return jsonify({"error": "Duration must be an integer"}), 400

    workouts.append({"workout": workout, "duration": duration})
    return jsonify({"message": f"{workout} added successfully!"}), 201

@app.route('/workouts', methods=['GET'])
def view_workouts():
    return jsonify({"workouts": workouts})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
