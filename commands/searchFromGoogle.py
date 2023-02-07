from Executando import criando_audio
import pesquisaNoGoogle
def pergunta(Swan):
    pergunta =  ''.join(Swan)
    resposta = pesquisaNoGoogle.obtendoResposta(pergunta,Swan)
    print(resposta)
    if resposta:
        criando_audio(resposta)
    else:
        criando_audio(Swan)
