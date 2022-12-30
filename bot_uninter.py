import telebot

CHAVE_API = "5646392598:AAHDK_kCgeAbJ5xGI_v4nin4JJWJCZlvch4"

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=["formulario"])
def pesquisa(mensagem):
    bot.send_message(mensagem.chat.id, "Para realizar a pesquisa acesse https://docs.google.com/forms/d/e/1FAIpQLSfsYKccUmt75S_8ibSlNK9QG8apw6lZKxeQeJRlNybU_MQfkQ/viewform")




@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    texto = """
    O que você deseja? (Clique em uma opção)
    /formulario Formulario"""

    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    bot.send_message(mensagem.chat.id, "Os aparelhos indicados para medir a pressão arterial https://sabiaescolha.com/melhor-medidor-de-pressao/")

@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    bot.send_message(mensagem.chat.id, "Central de ajuda https://sites.google.com/view/central-de-ajuda-cardiomed/p%C3%A1gina-inicial ou ligue 4099-9999")

@bot.message_handler(commands=["opcao4"])
def opcao3(mensagem):
    bot.send_message(mensagem.chat.id, "Saiba mais sobre hipertensão arterial https://cardiomedinformacoes.blogspot.com/2022/12/saude.html")



def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Escolha uma opção para continuar (Clique no item):
     /opcao1 Preencher o formulário diário
     /opcao2 Aparelhos indicados
     /opcao3 Central de Ajuda
     /opcao4 Saiba mais
Responder qualquer outra coisa não vai funcionar, clique em uma das opções"""
    bot.reply_to(mensagem, texto)

bot.polling()