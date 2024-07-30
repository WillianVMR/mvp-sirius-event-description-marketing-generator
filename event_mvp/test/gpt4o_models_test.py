from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Você é um copywriter especialista em divulgação de eventos cuja maior habilidade é criar textos de divulgação de eventos de alta qualidade que tem renome mundial."},
            {"role": "user", "content": "Crie uma descrição de um evento de música com o nome Metalica Brasil Tour que ira acontecer em Curitiba, Paraná, Brasil na data 12/12/2024 no horário 20:00 que irá ser um: show da banda metálica para relembrar os clássicos da banda"}
        ]    
    )
    
generated_description = completion.choices[0].message
    
print(generated_description)