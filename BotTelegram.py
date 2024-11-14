import telebot

CHAVE_API = "ADICIONE AQUI SUA CHAVE API"

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=["Smartphones"])
def pizza(mensagem):
    bot.send_message(mensagem.chat.id, "Aparelhos disponíveis:")

@bot.message_handler(commands=["Capas"])
def hamburguer(mensagem):
    bot.send_message(mensagem.chat.id, "Informe o modelo do seu aparelho e aguarde.")

@bot.message_handler(commands=["Peliculas"])
def salada(mensagem):
    bot.send_message(mensagem.chat.id, "Informe o modelo do seu aparelho e aguarde.")

@bot.message_handler(commands=["Fones de ouvido"])
def salada(mensagem):
    bot.send_message(mensagem.chat.id, "Aqui estão os modelos disponíveis:")

@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    texto = """
    Aqui está as principais opções: (Clique em uma opção)
    /Smartphones Smartphones
    /Capas Capas
    /Peliculas Peliculas
    /Fones de ouvido Fones de ouvido"""
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    bot.send_message(mensagem.chat.id, "Ok! Vamos direcionar você para a nossa assistência técnica. Informe o motivo do contato:")

@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    bot.send_message(mensagem.chat.id, "Informe o seu nome e o motivo do retorno/garantia")
    
@bot.message_handler(commands=["opcao4"])    
def opcao4(mensagem):
    bot.send_message(mensagem.chat.id, "Chat liberado para a realização do Feedback!")



def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Escolha uma opção que conrresponde com seu contato (Clique no item):
     /opcao1 Produtos
     /opcao2 Assistência técnica
     /opcao3 Retorno/Garantia
     /opcao4 Realizar um Feedback
Responder qualquer outra coisa não vai funcionar, clique em uma das opções"""
    bot.reply_to(mensagem, texto)

bot.polling() 