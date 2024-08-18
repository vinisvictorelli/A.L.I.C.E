import speech_recognition as sr

def reconhecimento_audio():
    try:
        audio = sr.Recognizer()
        with sr.Microphone() as source:
            audio.adjust_for_ambient_noise(source)
            print()
            print('-----------------------------')
            print('Ouvindo..')
            voz = audio.listen(source, 15, 20)
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()
        return comando
    except sr.exceptions.UnknownValueError:
        return ''
    except sr.exceptions.WaitTimeoutError:
        return ''