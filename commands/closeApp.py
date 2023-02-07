import subprocess
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