from flask import Flask
import requests

chuck = Flask(__name__)

@chuck.route('/',methods=['GET'])
def get_chuck_norris_jokes():

    api_url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(api_url).json()
    image_tag = "<img src=" + response['icon_url'] + " alt='Chucks Image'>"

    return "<strong>Random joke from chuck norris: </strong>" + response['value'] + image_tag

# https://api.chucknorris.io/jokes/random

if __name__ == "__main__":
    
    chuck.run()