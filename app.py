from flask import Flask
from flask_cors import CORS

from config import Config
from extensions import db, jwt, bcrypt


def create_app():

    app = Flask(__name__)

    # Load Config
    app.config.from_object(Config)

    # Enable CORS
    CORS(app)

    # Initialize Extensions
    db.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)

    # Import Models
    from models.user import User
    from models.course import Course
    from models.note import Note
    from models.quiz import Quiz
    from models.quiz_result import QuizResult
    from models.chat import Chat

    # Import Routes
    from routes.auth import auth_bp
    from routes.dashboard import dashboard_bp
    from routes.course import course_bp
    from routes.notes import notes_bp
    from routes.quiz import quiz_bp
    from routes.chatbot import chat_bp
    from routes.progress import progress_bp

    # Register Blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(course_bp)
    app.register_blueprint(notes_bp)
    app.register_blueprint(quiz_bp)
    app.register_blueprint(chat_bp)
    app.register_blueprint(progress_bp)

    print(app.url_map)

    # Home Route
    @app.route("/")
    def home():
        return {
            "status": "success",
            "message": "AI Smart Education Platform Backend Running..."
        }

    return app


app = create_app()


if __name__ == "__main__":

    with app.app_context():
        db.create_all()

    app.run(debug=True)


@app.route("/test")
def test():
    return {
        "message": "Test API Working"
    }