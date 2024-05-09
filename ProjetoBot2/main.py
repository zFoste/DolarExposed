import tweepy
# import datetime
# import requests
# import time
# import yfinance as yf

api = tweepy.Client (
consumer_key='PfOs01JjqE9HLgqbpiKdLE1GT',
consumer_secret='yTzsTHVFO7c3OnlmcEcruwtaaQATXFVxQdpHqNZetLYVc1qDLm',
access_token='1785330303986196481-eknco0L0Dhp1ulVMLCptIBPE7KGgqD',
access_token_secret='QotBJF96SJbIp5pgeXVY0RqMqjONv8EgzBmtDt9zbc0bB'
)

# horario_abertura = datetime.time(8, 0, 0)
# horario_fechamento = datetime.time(18, 0, 0)

auth = tweepy.OAuthHandler('PfOs01JjqE9HLgqbpiKdLE1GT', 'yTzsTHVFO7c3OnlmcEcruwtaaQATXFVxQdpHqNZetLYVc1qDLm')
auth.set_access_token('1785330303986196481-eknco0L0Dhp1ulVMLCptIBPE7KGgqD', 'QotBJF96SJbIp5pgeXVY0RqMqjONv8EgzBmtDt9zbc0bB')
api = tweepy.API(auth)

# def dentro_horario_comercial():
#     agora = datetime.datetime.now()
#     horario_atual = agora.time()
#     return horario_abertura <= horario_atual <= horario_fechamento

# def obter_cotacao_dolar():
#     simbolo_dolar = "USD=X"

#     try:
#         dados_dolar = yf.download(simbolo_dolar, period="1d", interval="1m")
#         valor_fechamento = dados_dolar["Close"].iloc[-1]
#         valor_formatado = "{:.2f}".format(valor_fechamento)

#         return valor_formatado
#     except Exception as e:
#         print(f"Erro ao obter cotação do dólar: {e}")
#         return None
# while True:
#     try:
#         if dentro_horario_comercial():
#             valor_dolar = obter_cotacao_dolar()
#             if valor_dolar:
#                 texto_tweet = f"Dólar agora: R$ {valor_dolar}"
#                 api.update_status(texto_tweet)
#                 print(f"Tweet publicado: {texto_tweet}")
#                 time.sleep(30)
#             else:
#                 time.sleep(46000) 
#     except Exception as e:
#         print(f"Erro geral durante a execução: {e}")
#         time.sleep(3600) 

try: 
    tweet = api.create_tweet(text="teste")
    print(tweet)
except: 
    print("algo falhou")