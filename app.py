from controllers.level_controllers import get_level
from endpoints import endpoints
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# ENDPOINT


@app.route('/api')
def healthcheck():
    return endpoints


@app.route('/api/level/<level_id>')
def level_level_id(level_id):
    print(level_id)
    return get_level(level_id)


if __name__ == '__main__':
    app.run()
