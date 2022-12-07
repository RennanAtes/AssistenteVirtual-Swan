
import Executando


def formatando(Swan,SwanFala):
    PalavrasChavesPesquisar = ['pesquisar', 'pesquise', 'pesquisa']
    PalavrasChavesYoutube = ['vídeo', 'vídeos', 'youtube']
    PalavrasChavesAbrir = ['abrir', 'abra', 'abre']
    PalavrasChavesFechar = ['fecha', 'fechar', 'feche']
    a = len(Swan)
    SwanFormatado = []
    chave = ""

    for i in range (0,a):
        if Swan[i] in PalavrasChavesPesquisar:
            SwanFormatado.append('pesquisa')
            print ("Aqui em baixo é o meu SwanFormatando")
            print (SwanFormatado)
        elif Swan[i] in PalavrasChavesYoutube:
            SwanFormatado.append('youtube')
            print ("Aqui em baixo é o meu SwanFormatando")
            print (SwanFormatado)
        elif Swan[i] in PalavrasChavesAbrir:
            SwanFormatado.append('abrir')
            print ("Aqui em baixo é o meu SwanFormatando")
            print (SwanFormatado)
        elif Swan[i] in PalavrasChavesFechar:
            SwanFormatado.append('fechar')
            print ("Aqui em baixo é o meu SwanFormatando")
            print (SwanFormatado)
    if 'pesquisa' in SwanFormatado:
        print ("A função pesquisar foi chamada")
        chave = 'pesquisa'
        Executando.Executar(Swan,chave,SwanFala)
    elif 'youtube' in SwanFormatado:
        print ("A função pesquisar foi chamada")
        chave = 'youtube'
        Executando.Executar(Swan,chave,SwanFala)
    elif 'abrir' in SwanFormatado:
        print ("A função pesquisar foi chamada")
        chave = 'abrir'
        Executando.Executar(Swan,chave,SwanFala)
    elif 'fechar' in SwanFormatado:
        print ("A função fechar foi chamada")
        chave = 'fechar'
        Executando.Executar(Swan,chave,SwanFala)