from flask import Flask, Response, request
import random

app = Flask(__name__)

@app.route('/char/classes', methods=['GET'])
def classes():
    class_list = ['Fighter', 'Wizard', 'Rogue']
    classes = random.choice(class_list)
    return Response(classes, mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)