from openai import OpenAI

client = OpenAI()

response = client.images.generate(
        model="dall-e-3",
        prompt="Crie um banner de divulgação de um evento de música com o nome Metalica Brasil Tour que ira acontecer em Curitiba, Paraná, Brasil na data 12/12/2024 no horário 20:00 que irá ser um: show da banda metálica para relembrar os clássicos da banda",
        size="1792x1024",
        quality="standard",
        n=1   
    )
    
image_url = response.data[0].url
    
print(image_url)