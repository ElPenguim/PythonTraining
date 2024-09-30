faq = {
    "Qual o seu nome?": "Meu nome é Prat's Bot", 
    "Qual a sua função?": "Fornecer conhecimento sobre a Prat's",
    "Qual seu suco favorito?": "Adoro todos mas em particular o de Goiaba",
    "Quais são os produtos disponiveis para venda?": "No momento vendenmos suco de ,laranja, goaiaba, uva e limão"
}

def carbot_responder(pergunta):

    resposta = faq.get(pergunta, "Desculpa, mas não entendi a pergunta")

    return resposta 

while True:

    pergunta_usuario = input("Você: ")

    if pergunta_usuario.lower () == "sair":
        print("Carbot encerrado.")
        break

    resposta_carbot = carbot_responder(pergunta_usuario)

    print("Carbot:", resposta_carbot)