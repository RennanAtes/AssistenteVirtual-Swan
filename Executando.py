
import webbrowser
import subprocess
google = "C:\Program Files\Google\Chrome\Application\chrome.exe"
def Executar(Swan,chave,SwanFala):
    print ("Função executar chamada.")
    if chave == 'pesquisa':
        pesquisa(SwanFala)
    elif chave == "youtube":
        youtube(SwanFala)
    elif chave == "abrir":
        abrir(Swan)
    elif chave == "fechar":
        fechar(Swan)
def pesquisa(SwanFala):
    print ("Função pesquisa chamada.")
    webbrowser.get('windows-default').open_new('https://www.google.com.br/search?q=' + f'{SwanFala}')
def youtube(SwanFala):
    print ("função youtube chamada")
    webbrowser.get('windows-default').open_new('https://www.youtube.com/results?search_query=' + f'{SwanFala}')
def abrir(Swan):
    if 'google' in Swan:
        subprocess.call([google])
def fechar(Swan):
    if 'google' in Swan:
        subprocess.call(["taskkill", "/F", "/IM", "chrome.exe"])