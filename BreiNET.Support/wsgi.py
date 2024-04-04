from src.config import EnvVar  # Import your environment variables class
from src.app import app  # Import your Flask application

env: EnvVar = EnvVar()  # Create an instance of your environment variables class

# Set up your Flask app configurations based on environment variables
app.config['PORT'] = env.port
app.config['ADDRESS'] = env.address
app.config['DEBUG'] = env.debug
app.config['SECRET_KEY'] = env.secret_key

if __name__ == '__main__':
    from gunicorn.app.wsgiapp import WSGIApplication
    class FlaskApp(WSGIApplication):
        def init(self, parser, opts, args):
            return {
                'bind': f"{env.address}:{env.port}",
                'workers': 2,
                'timeout': 120,
                'loglevel': 'info'
            }

        def load(self):
            return app

    FlaskApp().run()
