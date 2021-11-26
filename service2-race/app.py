from flask import Flask, Response, request
import random

app = Flask(__name__)

@app.route('/char/races', methods=['GET'])
def races():
    race_list = ['Human', 'Elf', 'Dragonborn']
    race = random.choice(race_list)
    return Response(race, mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)