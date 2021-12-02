#The various imports needed for this service to run including random from Python3
from flask import Flask, Response, request
import random

app = Flask(__name__)

#The Route that generates a random D&D class from a set list
@app.route('/char/classes', methods=['GET'])
def classes():
    class_list = ['Fighter', 'Wizard', 'Rogue']
    classes = random.choice(class_list)
    return Response(classes, mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)