from endpoints import endpoints
from flask import Flask

app = Flask(__name__)

# ENDPOINT


@app.route('/api')
def healthcheck():
    return endpoints


if __name__ == '__main__':
    app.run()
