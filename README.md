 # MoodMate Backend

MoodMate is a wellness app that helps users log their moods and receive personalized suggestions. This is the Flask-based backend that supports user authentication, mood tracking, and mood suggestions.

---

##  Live Demo

<!-- >  Deployed on: [https://moodmate-backend.onrender.com](https://moodmate-backend.onrender.com) -->

---

## Technoloy  used 

- **Flask**
- **SQLAlchemy**
- **SQLite** (local) / **PostgreSQL** (production)
- **CORS**
- **Render** (for deployment)

---

##  Project Structure

moodmate-backend/
├── app.py # Main Flask app
├── lib/
│ └── db/
│ ├── models.py # SQLAlchemy models (User, MoodLog)
│ └── base.py # Session and DB connection
├── static/ # React frontend (built files)
├── requirements.txt
└── README.md

yaml


---

## ⚙️ Local Setup Instructions

### 1. Clone the Repository

```bash```

git clone https://github.com/your-username/moodmate-backend.git
cd moodmate-backend
2. Set Up Virtual Environment
```bash```

python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
3. Install Requirements
```bash```

pip install -r requirements.txt
4. Run the App
```bash```

python app.py
The backend will be available at http://localhost:5000

 API Documentation
 POST /login
Create or return a user.

Request:
json

{
  "name": "Christina"
}
Response:
json

{
  "id": 1,
  "name": "Christina"
}
 POST /moods
Log a new mood and get a suggestion.

Request:
json

{
  "user_id": 1,
  "mood": "happy"
}
Response:
json

{
  "mood": "happy",
  "suggestion": "Treat yourself to something nice."
}
 GET /moods/<username>
Retrieve all mood logs for a specific user.

Example:
GET /moods/Christina

Response:
json

[
  {
    "id": 3,
    "mood": "happy",
    "suggestion": "Go out for a walk and smile at strangers.",
    "timestamp": "2025-05-31 14:22"
  },
  ...
]
 DELETE /moods/<int:id>
Delete a mood entry.

Example:
DELETE /moods/3

Response:
json

{
  "message": "Mood deleted successfully"
}
 Mood Suggestions
A sample of moods supported with built-in suggestions:

Happy

Sad

Angry

Anxious

Energetic

Tired

Frustrated

Hopeful

Content

Overwhelmed

Confident

Bored

Curious
(and more...)

 Testing with curl
```bash```

curl -X POST http://localhost:5000/login \
-H "Content-Type: application/json" \
-d '{"name": "Christina"}'
☁️ Deploying to Render
Push your code to GitHub.

Go to render.com.

Create a new Web Service:

Build Command:

```bash```

pip install -r requirements.txt
Start Command:

```bash```

gunicorn app:app
Add necessary environment variables (if using PostgreSQL).

Set the root directory to the project folder.

Enable auto-deploy on push (optional).

Hit "Deploy"!

   ### Notes
Make sure your frontend build files are in the static/ directory.

The backend is set up to serve a React frontend 

For production, connect PostgreSQL and update lib/db/base.py.

## Author
Christina Wachia Manga
📧 christinamanga98@gmail.com

## License
MIT

yaml


---







