import pyttsx3


def voiceReader(txt='Hello, World!'):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(txt)
    engine.runAndWait()
    return 0


if __name__ == '__main__':
    voiceReader()
