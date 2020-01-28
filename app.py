from flask import Flask
app = Flask(__name__)

# Initialising Environment Variables
from dotenv import load_dotenv
load_dotenv()

@app.route('/')
def hello_world():
    return 'Hello, World!'

def

if __name__ == '__main__':
    app.run()

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)