from distutils.debug import DEBUG
from src.app import create_app

app = create_app()
PORT = 4000
if __name__ == '__main__':
    app.run(port=PORT, host='0.0.0.0', debug=True)
