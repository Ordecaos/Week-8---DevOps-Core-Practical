#The various imports needed for this service to run including random from Python3
from flask import Flask, Response, request
import random

app = Flask(__name__)

#This route takes information from service 2 and further generates information from that, choosing a from a list of 3 names per race
@app.route('/char/name', methods=['POST'])
def names():
    race = request.data.decode('utf-8')
    if race == 'Human':
        human_list = ['Om', 'Vardam', 'Sondisk']
        name = random.choice(human_list)
    elif race == 'Elf':
        elf_list = ['Beiran', 'Pakian', 'Zinyarus']
        name = random.choice(elf_list)
    elif race == 'Dragonborn':
        dragonborn_list = ['Paravax', 'Faccethir', 'Krochuas']
        name = random.choice(dragonborn_list)
    return Response(name, mimetype='text/plain')

#This route takes information from service 3 and generates a title based on the class generated
@app.route('/char/title', methods=['POST'])
def titles():
    classes = request.data.decode('utf-8')
    if classes=="Fighter":
        fighter_list =['Brave', 'Strong', 'Tactical']
        title = random.choice(fighter_list)
    elif classes=="Wizard":
        wizard_list = ['Wise', 'Powerful', 'Devious']
        title = random.choice(wizard_list)
    elif classes=="Rogue":
        rogue_list = ['Cunning', 'Cutthroat', 'Silent']
        title = random.choice(rogue_list)
    return Response(title, mimetype='text/plain')
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)