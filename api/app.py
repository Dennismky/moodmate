from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from lib.db.models import User, MoodLog
from lib.db.base import session
from datetime import datetime
import os
import random

app = Flask(__name__, static_folder="static", static_url_path="")
CORS(app)

# Mood suggestions
SUGGESTIONS = {
    "happy": ["Go out for a walk and smile at strangers.", "Treat yourself to something nice."],
    "sad": ["Call someone you trust.", "Write your thoughts in a journal."],
    "angry": ["Take deep breaths.", "Listen to calming music."],
    "jovial": ["Share your joy with someone!", "Dance it out."],
    "anxious": ["Try a breathing exercise.", "Watch a comforting movie."],
    "energetic": ["Use your energy to start a new project!", "Go exercise!"],
    "tired": ["Take a nap.", "Have a glass of water and rest."],
    "frustrated": ["Step away and breathe.", "Talk to a friend."],
    "hopeful": ["Visualize your goals.", "Take one small action."],
    "content": ["Celebrate this peace.", "Share it with someone."],
    "nervous": ["Focus on the present.", "Try a grounding technique."],
    "relaxed": ["Enjoy the moment.", "Keep doing what you're doing."],
    "overwhelmed": ["Break tasks down.", "Pause and reset."],
    "inspired": ["Create something!", "Write down your ideas."],
    "lonely": ["Reach out to someone.", "Join a community online."],
    "grateful": ["Write a gratitude list.", "Tell someone you appreciate them."],
    "bored": ["Try something new.", "Learn a random fact."],
    "confident": ["Tackle that big task!", "Speak your mind."],
    "restless": ["Move your body.", "Channel it into creativity."],
    "curious": ["Research a new topic.", "Ask questions."]
}


@app.route("/")
def index():
    return {"message": "MoodMate API is running!"}


@app.route("/login", methods=["POST"])
def login():
    name = request.json.get("name")
    user = session.query(User).filter_by(name=name).first()
    if not user:
        user = User(name=name)
        session.add(user)
        session.commit()
    return jsonify({"id": user.id, "name": user.name})


@app.route("/moods", methods=["POST"])
def log_mood():
    data = request.json
    user_id = data.get("user_id")
    mood = data.get("mood")

    suggestion = random.choice(SUGGESTIONS.get(mood.lower(), ["Take a moment for yourself."]))
    log = MoodLog(user_id=user_id, mood=mood.lower(), suggestion=suggestion, timestamp=datetime.now())
    session.add(log)
    session.commit()

    return jsonify({"mood": mood, "suggestion": suggestion})


@app.route("/moods/<username>", methods=["GET"])
def get_logs(username):
    user = session.query(User).filter_by(name=username).first()
    if not user:
        return jsonify([])

    logs = session.query(MoodLog).filter_by(user_id=user.id).order_by(MoodLog.timestamp.desc()).all()
    return jsonify([
        {
            "id": log.id,
            "mood": log.mood,
            "suggestion": log.suggestion,
            "timestamp": log.timestamp.strftime("%Y-%m-%d %H:%M")
        }
        for log in logs
    ])


@app.route('/moods/<int:mood_id>', methods=['DELETE'])
def delete_mood(mood_id):
    mood_log = session.get(MoodLog, mood_id)
    if not mood_log:
        return jsonify({"error": "Mood not found"}), 404

    session.delete(mood_log)
    session.commit()
    return jsonify({"message": "Mood deleted successfully"}), 200


# Serve React frontend
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve_react(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, "index.html")


if __name__ == "__main__":
    app.run(port=5000, debug=True)

