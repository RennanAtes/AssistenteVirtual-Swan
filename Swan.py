import speech_recognition as sr
import texto
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
def Tratamento(SwanFala):
    Quebrar = SwanFala.split()
    QuantasPalavras = len(Quebrar)
    Swan = []
    for i in range (0,QuantasPalavras):
        Quebrar[i] = Quebrar[i].lower()
        Swan.append(Quebrar[i])
    print (Swan)
    texto.formatando(Swan,SwanFala)

while True:
    def Looping():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Reconhecendo...")
            audio = r.listen(source, phrase_time_limit=2)
        try:
            query = r.recognize_google(audio, language='en-us')
            print (query)
            if 'swan' in query:
                Reconhecimento()
        except Exception as e:
            Looping()
    Looping()