from flask import ( Blueprint , render_template )
import json 

bp = Blueprint('pet', __name__, url_prefix="/pets")
pets = json.load(open('pets.json', encoding="UTF-8"))

@bp.route('/')
def index(): 
    return render_template('index.html', pets=pets)

@bp.route('/<int:id>')
def show(id):
    pet = pets[id - 1]
    return render_template('show.html', pet=pet)