import telepot
import json
from telepot.namedtuple import ForceReply, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

load = open("token.json")   
token = json.loads(load.read()) 
bot = telepot.Bot(token['token'])   


def condicoes(chatID, msg):
            if(msg == '/start'):
                    inicio(chatID, bot)

########################### Guia
            elif(msg == 'Paraibuna'):
                    bot.sendMessage(
                        chatID,
                        "Entreterimento da Cidade de Paraibuna",
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Gastronomia tipica", callback_data='GT')],
                                [InlineKeyboardButton(text="Restaurantes", callback_data='REST')],
                                [InlineKeyboardButton(text="Eventos Da Cidade", callback_data='EDC')],
                                [InlineKeyboardButton(text="Igrejas", callback_data='IG')],
                                [InlineKeyboardButton(text="Guia Turistico para Cidade", callback_data='GTC')],
                                            ]
                        )
                    )
            elif(msg == 'GT'):
                bot.sendMessage(chatID, "Todos os pratos tipicos da Cidade: ")
                doc = open ("Gastronomia Tipica/GastronomiaTI.pdf",'rb')
                bot.sendDocument(chatID, doc)
                doc.close()
            
            elif(msg == 'REST'):
                    txt = open('Restaurantes/REST.md','r')
                    bot.sendMessage(
                        chatID,
                        txt.read(),
                        'Markdown',
                        reply_markup=InlineKeyboardMarkup(
                    
                        )
                    )
                    txt.close()


            elif(msg =='EDC'):
                txt = open('Eventos/EDC.md','r')
                bot.sendMessage(
                    chatID,
                    txt.read(),
                    'Markdown',
                    reply_markup=InlineKeyboardMarkup(
                            
                        )
                    )
                txt.close()

                
            elif(msg == 'IG'):
                 bot.sendMessage(chatID, "Igrejas em Paraibuna")
                 doc = open ("Igrejas/IgrejasPAB.pdf",'rb')
                 bot.sendDocument(chatID, doc)
                 doc.close()


            
            elif(msg == 'GTC'):
                bot.sendMessage(chatID, "Alguns dos passeios existentes em Paraibuna")
                doc = open ("Guia/LVP.pdf",'rb')
                bot.sendDocument(chatID, doc)
                doc.close()

            


########################### Como chegar
            elif (msg == 'Como Chegar'):
                    txtHelp = open('ComoChegar/Textos/txt01.md','r')

                    keyboard=ReplyKeyboardMarkup(
                        keyboard=[
                            [
                                KeyboardButton(text="Paraibuna no Mapa"),
                                KeyboardButton(text="Imagens"),
                                KeyboardButton(text="Voltar")
                            ]
                        ],
                        resize_keyboard=True
                    )

                    bot.sendMessage(chatID,	txtHelp.read(),'Markdown', reply_markup=keyboard)

                    txtHelp.close()	#Fecha o arquivo

            elif(msg == 'Paraibuna no Mapa'):
                    bot.sendMessage(chatID,"Enviando localização...")
                    bot.sendLocation(chatID, -23.3814,-45.6626)
                    
            elif(msg=='Imagens'):
                doc = open ("SobreParaibuna/ImgP/PAB.jpg",'rb')
                bot.sendDocument(chatID, doc)
                doc.close()



                
##########################################################################################################

########################### Sobre Paraibuna
            elif (msg == 'Sobre Paraibuna'):
                    txtHelp = open('SobreParaibuna/Textos/introducaoSobreParaibuna.md','r')
                    keyboard=ReplyKeyboardMarkup(
                        keyboard=[
                            [
                                KeyboardButton(text="+ Sobre Paraibuna"),
                                KeyboardButton(text="Departamentos"),
                                KeyboardButton(text="Voltar")
                            ]
                        ],resize_keyboard=True
                    )
                    bot.sendMessage(chatID, txtHelp.read(), 'Markdown', reply_markup=keyboard)
                    txtHelp.close()

            elif (msg == '+ Sobre Paraibuna'):
                    txtHelp = open('SobreParaibuna/Textos/sobreParaibuna.md','r')
                    bot.sendMessage(chatID, txtHelp.read(), 'Markdown')
                    txtHelp.close()

            elif (msg =='Departamentos'):
                txtHelp = open('SobreParaibuna/Departamentos/depart.md','r')
                bot.sendMessage(chatID, txtHelp.read(), 'Markdown')
                txtHelp.close()
                

           

##########################################################################################################

            elif (msg == 'Voltar'):
                    inicio(chatID, bot)

def callback(msg):
            query_id, from_id, query_data = telepot.glance(msg, flavor="callback_query")
            
            chatID = from_id
            
            texto = query_data
           

            print(chatID)

            bot.answerCallbackQuery(query_id, text="Só um instante")
            

            print("callback query", query_id, from_id, query_data)

            condicoes(chatID, texto)
            



def ir(msg):
            #Forma facilitada pela biblioteca "telepot" de quebrar inserir as informacoes para as respectivas variaveis
            #Ou seja, pega o Json com a chave 'chat' e quebra as informacoes em tres jogando o valor de 'text' para a variavel tipoMsg,
            #assim por adiante...
            tipoMsg, tipoChat, chatID = telepot.glance(msg)

                #variavel Auxiliar para receber a texto que o usuario digitou, fiz ela porque se eu chamasse --condicoes(chatID, msg['text'])--
                                    #tava dando erro

            condicoes(chatID, msg['text'])    # pega o que foi digitado pelo usuario e seu ID manda para a funcao 'condicoes' que vai processar o a mensagem


def inicio(chatID, bot):
            keyboard=ReplyKeyboardMarkup(
                        keyboard=[
                            [
                                KeyboardButton(text="Paraibuna"),
                                KeyboardButton(text="Como Chegar"),
                                KeyboardButton(text="Sobre Paraibuna"),
                            ]
                        ],resize_keyboard=True
                    )

            txt = open('Inicializacao/Hello.md','r')    #Abre o arquivo Hello.md com o atributo leitura
            bot.sendMessage(chatID,txt.read(),'Markdown',reply_markup=keyboard)
            txt.close()

bot.message_loop(
    {
        'chat': ir,
        'callback_query': callback,
    }
)

#responsavel por deixa o programa sempre em execucao, mas quando ocorre uma interacao, o message_loop e invocado, e quebra este laco infinito,
#e faz o comportamento requirido pelo usuario
while True:
            pass
