import webbrowser
def youtube(Swan):
    PalavraDeletarChave = ['vídeo', 'vídeos', 'youtube']
    Swan2 = Swan
    if Swan[0] in PalavraDeletarChave:
        Swan2.remove(Swan[0])
    Apesquisa =  ' '.join(Swan2)
    print (Apesquisa)
    print ("função youtube chamada")
    webbrowser.get('windows-default').open_new('https://www.youtube.com/results?search_query=' + f'{Apesquisa}')