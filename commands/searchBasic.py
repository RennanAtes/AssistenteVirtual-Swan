import webbrowser
def pesquisa(Swan):
    PalavraDeletarChave = ['pesquisar', 'pesquise', 'pesquisa']
    Swan2 = Swan
    if Swan[0] in PalavraDeletarChave:
        Swan2.remove(Swan[0])
    Apesquisa =  ''.join(Swan2)
    print (Apesquisa)
    webbrowser.get('windows-default').open_new('https://www.google.com.br/search?q=' + f'{Apesquisa}')