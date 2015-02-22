import speech_recognition as sr

__author__ = 'tclass'


class Recognizer:

    def __init__(self):
        self.recognizer = sr.Recognizer()

    def recognize(self):

        with sr.Microphone() as source:  # use the default microphone as the audio source
            audio = self.recognizer.listen(source)  # listen for the first phrase and extract it into audio data

        try:
            recognize_list = self.recognizer.recognize(audio, True)  # generate a list of possible transcriptions
            print("Possible transcriptions:")
            for prediction in recognize_list:
                print(" " + prediction["text"] + " (" + str(prediction["confidence"]*100) + "%)")
        except LookupError: # speech is unintelligible
            print("Could not understand audio")
            return "dummy"
        return recognize_list.pop(0)["text"]