from flask import Flask, request, jsonify
from flask_cors import CORS
from lib.db.models import User, MoodLog
from lib.db.base import session
from datetime import datetime
import random

app = Flask(__name__)
CORS(app)

# Mood suggestions
SUGGESTIONS = {
    "happy": ["Go out for a walk and smile at strangers.", "Treat yourself to something nice."],
    "sad": ["Call someone you trust.", "Write your thoughts in a journal."],
    "angry": ["Take deep breaths.", "Listen to calming music."],
    "jovial": ["Share your joy with someone!", "Dance it out."],
    "anxious": ["Try a breathing exercise.", "Watch a comforting movie."]
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

if __name__ == "__main__":
    app.run(port=5000, debug=True)

