#The various imports needed for this service to run, this incldes flask, SQLalchemy and requests.
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
import requests

app = Flask(__name__)

#The SQL set up
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///char.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#The table used to store up to 5 of the latest characters generated
class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dbrace = db.Column(db.String(225), nullable=False)
    dbclass = db.Column(db.String(225), nullable=False)
    dbname = db.Column(db.String(225), nullable=False)
    dbtitle = db.Column(db.String(225), nullable=False)

#This is the route for the homepage
@app.route('/')
def home():
     return render_template('index.html')

#This is the route for the generator as well as displaying the 5 last generated names and titles
@app.route('/generator', methods=['GET'])
def generator():
    race = requests.get('http://service2-race:5000/char/races')
    classes = requests.get('http://service3-classes:5000/char/classes')
    name = requests.post('http://service4-name:5000/char/name', data=race.text)
    title = requests.post('http://service4-name:5000/char/title', data=classes.text)

    last_five_characters = Characters.query.order_by(Characters.id.desc()).limit(5).all()
    db.session.add(
        Characters(
            dbrace = race.text,
            dbclass = classes.text,
            dbname = name.text,
            dbtitle = title.text
        )
    )
    db.session.commit()
    
    return render_template('generator.html', race=race.text, classes=classes.text, name=name.text, title=title.text, last_five_characters=last_five_characters)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)