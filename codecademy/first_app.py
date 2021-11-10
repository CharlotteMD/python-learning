from flask import Flask
from helper import pets

app = Flask(__name__)

@app.route('/')
def index():
  html = '''<h1>Adopt a Pet!</h1>
    <p>Browse through the links below to find your new furry friend: </p>'''
  for animal in pets:
    animals_list = f'<li><a href="/animals/{animal}">{animal}</a></li>'
    html += animals_list
  return html

@app.route('/animals/<pet_type>')
def animals(pet_type):
  pet_list = pets[pet_type]
  html = f'<h1>List of {pet_type}</h1>'
  for idx, animal in enumerate(pets[pet_type]):
    animal_name = animal['name']
    html += f'<li><a href="/animals/{pet_type}/{idx}">{animal_name}</a></li>'
  return html

@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
  pet_list = pets[pet_type]
  pet = pet_list[pet_id]
  pet_image = pet["url"]
  html = f'<h1>{pet["name"]}</h1><img src="{pet_image}"/><p>{pet["description"]}</p><ul><li>{pet["breed"]}</li><li>{pet["age"]}</li></ul>'
  return html
