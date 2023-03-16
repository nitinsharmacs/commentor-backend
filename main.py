from distutils.debug import DEBUG
from src.app import create_app

app = create_app()
PORT = 3000
if __name__ == '__main__':
    app.run(port=PORT, debug=True)
