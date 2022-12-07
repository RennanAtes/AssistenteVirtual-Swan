
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
