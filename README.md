# MoodMate Backend

**MoodMate** is a wellness app that lets users log moods and receive personalized suggestions for emotional well-being. This Flask-based backend powers user authentication, mood tracking, and mood-based suggestions.

---

## Live Demo

- **Backend**: [https://moodmate-6-z0a4.onrender.com](https://moodmate-6-z0a4.onrender.com)  
- **Frontend**: [https://moodmate-frontend.netlify.app](https://moodmate-frontend.netlify.app)

---

## Technologies Used

- `Flask`
- `SQLAlchemy`
- `SQLite` (development)
- `PostgreSQL` (production)
- `CORS`
- `Render` (deployment)

---

## Features

- User login 
- Mood logging with personalized suggestions
- Fetch user-specific mood history
- Delete mood entries by ID
 - Filter mood logs by date or mood
 - Update mood logs
- CLI tools for database management
- Serves built React frontend from `/static/`

---

## Project Structure

```plaintext
moodmate-backend/
├── app.py                  # Main Flask application
├── lib/
│   └── db/
│       ├── models.py       # SQLAlchemy models: User, MoodLog, Suggestion
│       └── base.py         # DB setup and session config
├── cli.py                  # CLI for DB operations
├── static/                 # Compiled React frontend
├── requirements.txt
└── README.md

## Local Setup Instructions

1. Clone the Repository
```bash```
      git clone https://github.com/your-username/moodmate.git

       cd moodmate

2. Set Up a Virtual Environment
```bash```
   python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
3. Install Dependencies
```bash```
    pip install -r requirements.txt
4. Run the App
```bash```
    python app.py
 Visit: http://localhost:5000

## CLI Tool for Database Management

1.Create Tables
```bash```
  python cli.py create

2.Seed the Database
```bash```
    python cli.py seed
3.Drop and Recreate Tables
```bash```
   python cli.py reset

## API Endpoints

Method	Endpoint	Description
GET	/	Welcome message
POST	/login	Create or log in a user
POST	/moods	Log a new mood
GET	/moods/<username>	Fetch moods for a user
DELETE	/moods/<int:mood_id>	Delete mood by ID

## POST /login
1.Request
json

{
  "name": "Christina"
}
Response
json

{
  "id": 1,
  "name": "Christina"
}
 POST /moods
Request
json

{
  "user_id": 1,
  "mood": "happy"
}
Response
json

{
  "mood": "happy",
  "suggestion": "Treat yourself to something nice."
}
 GET /moods/<username>
Example
bash

GET /moods/Christina
Response
json

[
  {
    "id": 3,
    "mood": "happy",
    "suggestion": "Go out for a walk and smile at strangers.",
    "timestamp": "2025-05-31 14:22"
  }
]
 DELETE /moods/<int:id>
Example
```bash```
DELETE /moods/3
Response
json

{
  "message": "Mood deleted successfully"
}
 Supported Moods & Suggestions
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
... and more!

## Testing with curl
bash

curl -X POST http://localhost:5000/login \
-H "Content-Type: application/json" \
-d '{"name": "Christina"}'

## Deploying to Render
- Push code to GitHub

- Go to render.com and create a new Web Service

- Set the following:

- Build Command:
``bash``
   pip install -r requirements.txt
- Start Command:
```bash```
   gunicorn api.app:app
- Add environment variables as needed (e.g., for PostgreSQL)

- Ensure frontend build is in the /static/ folder

- Deploy

## Authors
1.Dennis Muasya

2.Christina Wachia Manga

3.Vallery Jepleting

## License
Licensed under the MIT License

