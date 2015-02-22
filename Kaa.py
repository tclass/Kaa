import Recognizer
import CommandMatcher

__author__ = 'tclass'
version = "0.1"
config_file = "config.cfg"


def main():
    c = CommandMatcher.CommandMatcher(config_file)

    r = Recognizer.Recognizer()
    sentence = r.recognize()

    c.match_with_sentence(sentence)

main()