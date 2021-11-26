from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
     return render_template('index.html')

@app.route('/generator', methods=['GET'])
def generator():
    race = requests.get('http://service2-race:5000/char/races')
    classes = requests.get('http://service3-classes:5000/char/classes')
    name = requests.post('http://service4-name:5000/char/name', data=race.text)
    title = requests.post('http://service4-name:5000/char/title', data=classes.text)
    return render_template('generator.html', race=race.text, classes=classes.text, name=name.text, title=title.text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)