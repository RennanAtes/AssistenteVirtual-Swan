
import webbrowser
import subprocess
from gtts import gTTS
import pesquisaNoGoogle
from playsound import playsound
google = "C:\Program Files\Google\Chrome\Application\chrome.exe"
def Executar(Swan,chave,SwanFala):
    print ("Função executar chamada.")
    if chave == 'pesquisa':
        pesquisa(Swan)
    elif chave == "youtube":
        youtube(Swan)
    elif chave == "abrir":
        abrir(Swan)
    elif chave == "fechar":
        fechar(Swan)
    elif chave == "pergunta":
        pergunta(Swan)

        
def pesquisa(Swan):
    PalavraDeletarChave = ['pesquisar', 'pesquise', 'pesquisa']
    Swan2 = Swan
    if Swan[0] in PalavraDeletarChave:
        Swan2.remove(Swan[0])
    Apesquisa =  ' '.join(Swan2)
    print (Apesquisa)
    webbrowser.get('windows-default').open_new('https://www.google.com.br/search?q=' + f'{Apesquisa}')
def youtube(Swan):
    PalavraDeletarChave = ['vídeo', 'vídeos', 'youtube']
    Swan2 = Swan
    if Swan[0] in PalavraDeletarChave:
        Swan2.remove(Swan[0])
    Apesquisa =  ' '.join(Swan2)
    print (Apesquisa)
    print ("função youtube chamada")
    webbrowser.get('windows-default').open_new('https://www.youtube.com/results?search_query=' + f'{Apesquisa}')
def abrir(Swan):
    if 'google' in Swan:
        subprocess.call([google])
def fechar(Swan):
    if 'google' in Swan:
        subprocess.call(["taskkill", "/F", "/IM", "chrome.exe"])
    else:
        if 'fechar' in Swan:
            Swan.remove("fechar")
        if 'ópera' in Swan:
            Swan.remove("ópera")
            Swan.append("opera")
        Apesquisa =  ' '.join(Swan)
        print (Apesquisa)
        print (f"Vizualizando o Swan: {Swan}")
        subprocess.call(["taskkill", "/F", "/IM", (f"{Apesquisa}.exe")])
def Calculo(rs):
    rs = str(rs)
    print ("Função calculo com a resposta foi acionada.")
    criando_audio(rs)


def criando_audio(audio):
    tts = gTTS(audio, lang='pt-br')
    tts.save('audios/audio.mp3')
    print("Aprendendo oque você está falando.")
    playsound('audios/audio.mp3')

def pergunta(Swan):
    pergunta =  ' '.join(Swan)
    resposta = pesquisaNoGoogle.obtendoResposta(pergunta)
    criando_audio(resposta)
