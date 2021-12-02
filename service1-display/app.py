from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SelectField, SubmitField
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///char.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = ${secretkey}

db = SQLAlchemy(app)

class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dbrace = db.Column(db.String(225), nullable=False)
    dbclass = db.Column(db.String(225), nullable=False)
    dbname = db.Column(db.String(225), nullable=False)
    dbtitle = db.Column(db.String(225), nullable=False)

class PlayersTable(db.Model):
    Player_ID = db.Column(db.Integer, primary_key = True)
    Player_name = db.Column(db.String(255))
    Character_Name = db.Column(db.String(255))
    Character_Level = db.Column(db.Integer)
    Character_Class = db.Column(db.String(255))
    Character_Race = db.Column(db.String(255))

class Add_Player(FlaskForm):
    
    Player_name = StringField("Your Name")
    Character_Name = StringField("Character Name")
    Character_Level = SelectField("Character Level", choices=[(1), (2), (3), (4), (5), (6), (7), (8), (9), (10), (11), (12), (13), (14), (15), (16), (17), (18), (19), (20)])
    Character_Class = SelectField("Character Class", choices=[('Artificer', 'artificer'), ('Barbarian', 'barbarian'), ('Bard', 'bard'), ('Blood Hunter', 'blood hunter'), ('Cleric', 'cleric'), ('Druid', 'druid'), ('Fighter', 'fighter'), ('Monk', 'monk'), ('Paladin', 'paladin'), ('Ranger', 'ranger'), ('Rogue', 'rogue'), ('Sorcerer', 'sorcerer'), ('Warlock', 'warlock'), ('Wizard', 'wizard')])
    Character_Race = StringField("Character Race")
    submit = SubmitField("Add Player")

class Update_Player(FlaskForm):

    Player_name = StringField("Your Name")
    Character_Name = StringField("Character Name")
    Character_Level = SelectField("Character Level", choices=[(1), (2), (3), (4), (5), (6), (7), (8), (9), (10), (11), (12), (13), (14), (15), (16), (17), (18), (19), (20)])
    Character_Class = SelectField("Character Class", choices=[('Artificer', 'artificer'), ('Barbarian', 'barbarian'), ('Bard', 'bard'), ('Blood Hunter', 'blood hunter'), ('Cleric', 'cleric'), ('Druid', 'druid'), ('Fighter', 'fighter'), ('Monk', 'monk'), ('Paladin', 'paladin'), ('Ranger', 'ranger'), ('Rogue', 'rogue'), ('Sorcerer', 'sorcerer'), ('Warlock', 'warlock'), ('Wizard', 'wizard')])
    Character_Race = StringField("Character Race")
    submit = SubmitField("Update Player")

@app.route('/')
def home():
     return render_template('index.html')

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

@app.route('/Players')
def Player_Page():
    pla_id = PlayersTable.query.all()
    return render_template('Players.html', records=pla_id)

@app.route('/PlayerDetails/<int:Player_ID>')
def Player_Info(Player_ID):
    data = PlayersTable.query.filter_by(Player_ID=Player_ID).first()
    return render_template("Playerinfo.html", record=data)

@app.route('/Playerinput', methods=["GET", "POST"])
def Add_Players():
    form = Add_Player()
    if request.method == 'POST':
        Name=form.Player_name.data
        Character_Name=form.Character_Name.data
        Character_Level=form.Character_Level.data
        Character_Class=form.Character_Class.data
        Character_Race=form.Character_Race.data
        NewPlayer = PlayersTable(Player_name=Name, Character_Name=Character_Name, Character_Level=Character_Level, Character_Class=Character_Class, Character_Race=Character_Race, Campaign_In=Campaign_In)
        db.session.add(NewPlayer)
        db.session.commit()
        return redirect("/Players")
    return render_template("Playerinput.html", form=form)

@app.route('/PlayerEdit/<int:Player_ID>', methods=["GET", "POST"])
def Edit_Player(Player_ID):
    form = Update_Player()
    pla = PlayersTable.query.filter_by(Player_ID=Player_ID).first()
    if request.method == 'POST':
        pla.Player_name=form.Player_name.data
        pla.Character_Name=form.Character_Name.data
        pla.Character_Level=form.Character_Level.data
        pla.Character_Class=form.Character_Class.data
        pla.Character_Race=form.Character_Race.data
        db.session.commit()
        return redirect("/Players")
    return render_template("Playerinput.html", form=form)

@app.route('/PlayerDelete/<int:Player_ID>')
def Delete_Player(Player_ID):
    pla = PlayersTable.query.filter_by(Player_ID=Player_ID).first()
    db.session.delete(pla)
    db.session.commit()
    return redirect("/Players")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)