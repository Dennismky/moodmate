# MoodMate

MoodMate is a full-stack mood tracker app built with **Flask (Python)** on the backend and **React (JavaScript)** on the frontend. Users can log their moods, get mood-based suggestions, and track their emotional journey over time.

## Tech Stack

- **Frontend:** React + Vite
- **Backend:** Flask + SQLAlchemy
- **Database:** SQLite
- **Package Managers:** Pipenv (Python) & npm (Node.js)
- **API Communication:** REST (Fetch)

## Requirements

Ensure you have the following installed:

- Python 3.8+
- Pipenv (install via `pip install pipenv`)
- Node.js & npm (https://nodejs.org)
- Git

## Getting Started

1 . Clone the Repository

    ```bash
    git clone https://github.com/your-username/moodmate.git
    cd moodmatey
    
2  Set Up the Backend

    cd api
    pipenv install flask flask-cors sqlalchemy

 . If your code uses a custom module in lib/, set the project path:
        export PYTHONPATH=.

    Run the backend server:
        PYTHONPATH=. pipenv run python app.py
         The backend will start at: http://127.0.0.1:5000

3  Set Up the Frontend

    In a new terminal:
        cd moodmate/frontend
        npm install

Start the development server:
        npm run dev
        The frontend will start at: http://localhost:5173


        APPLICATION USAGE:

1 Visit http://localhost:5173 in your browser.

2 Enter your name to log in.

3 Select a mood from the dropdown and click Submit Mood.

4 A suggestion will appear based on your mood.

5 Your mood history will display below.

6 You can also delete a past mood log using the Delete icon.



 API Endpoints

Method	    Endpoint	        Description
POST	    /login	            Log in or create a new user
POST	    /moods	            Log a new mood
GET	        /moods/<username>	Fetch mood logs for a user
DELETE	    /moods/<mood_id>	Delete a mood log by ID


Sample Moods

Happy

Sad

Angry

Jovial

Anxious

Energetic


TROUBLESHOOTING

❌ ModuleNotFoundError: No module named 'flask'
→ Run pipenv install flask inside the api/ directory.

❌ npm run dev fails
→ Make sure you're in frontend/ and you've run npm install.

❌ CORS issues
→ Ensure flask-cors is installed and properly configured in app.py.


