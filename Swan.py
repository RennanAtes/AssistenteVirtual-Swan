def Reconhecimento():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print ("Ouvindo...")
        audio = r.listen(source)
    try:
        print ("Reconheceu...")
        query = r.recognize_google(audio, language='pt-br')
        print (query)
        SwanFala = query
        if query:
            Tratamento(SwanFala)

    except Exception as e:
        print (e)
        print ("Nenhum som foi reconhecido.")
        return "None"
    return query
Reconhecimento()