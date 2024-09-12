import microphone as microphone
import speech_recognition as r
def record_and_recognize_audio(*args: tuple):
    """
    Запись и распознавание аудио
    """
    with r.Microphone(device_index=2):
        recognized_data = ""

        # регулирование уровня окружающего шума
        r.adjust_for_ambient_noise(microphone, device_index=2)

        try:
            print("Listening...")
            audio = r.listen(microphone, 5, 5)

        except speech_recognition.WaitTimeoutError:
            print("Can you check if your microphone is on, please?")
            return

        # использование online-распознавания через Google
        try:
            print("Started recognition...")
            recognized_data = r.recognize_google(audio, language="ru").lower()

        except speech_recognition.UnknownValueError:
            pass

        # в случае проблем с доступом в Интернет происходит выброс ошибки
        except speech_recognition.RequestError:
            print("Check your Internet Connection, please")

        return recognized_data

record_and_recognize_audio()