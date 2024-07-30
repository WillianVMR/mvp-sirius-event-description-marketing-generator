from flask import Flask, render_template, request, redirect, url_for
from openai import OpenAI
import os
from datetime import datetime
import requests


client = OpenAI()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('create_event.html') # original render_template('create_event.html')

@app.route('/create_event', methods=['POST'])
def create_event():
    event_name = request.form['event_name']
    event_date = request.form['event_date']
    event_time = request.form['event_time']
    address_location = request.form['address_location']
    event_category = request.form['event_category']
    event_capacity = request.form['event_capacity']
    event_description = request.form['event_description']

    # Generate event description using OpenAI API
    
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Você é um copywriter especialista em divulgação de eventos cuja maior habilidade é criar textos de marketing de alta qualidade que tem renome mundial, seu objetivo é fazer as pessoas brilharem os olhos ao lerem o texto e despertar a vontade de comprar um ingresso, a partir da descrição abaixo abaixo ira gerar o copiwriting de divulgação de uma div estilizado para ser apresentado em uma página web dentro de uma div."},
            {"role": "user", "content": f"Crie uma descrição de um evento de {event_category} com o nome {event_name} que ira acontecer no endereço {address_location} na data {event_date} no horário {event_time} que irá ser de acordo com essa breve descrição: {event_description}"}
        ]    
    )
    
    generated_description = completion.choices[0].message.content

    # Generate event banner image using DALL-E API (hypothetical)
    
    response = client.images.generate(
        model="dall-e-3",
        prompt=f"Crie um banner de divulgação de um evento de {event_category} com o nome {event_name} que irá ser um: {event_description}",
        size="1792x1024",
        quality="standard",
        n=1   
    )
    
    image_url = response.data[0].url

    # Save image locally
    image_path = os.path.join('static/images', f"{event_name.replace(' ', '_')}.png")
    img_data = requests.get(image_url).content
    with open(image_path, 'wb') as handler:
        handler.write(img_data)
    

    event_data = {
        'name': event_name,
        'date': event_date,
        'time': event_time,
        'location': address_location,
        'category': event_category,
        'capacity': event_capacity,
        'description': generated_description,
        'image_path': image_path
    }

    return render_template('event_page.html', event=event_data)

if __name__ == '__main__':
    app.run(debug=True)
