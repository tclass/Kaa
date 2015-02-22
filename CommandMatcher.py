import ConfigParser
import os

__author__ = 'tclass'


class CommandMatcher:

    def __init__(self, filename):
        self.filename = filename
        self.config = ConfigParser.ConfigParser()

    def match_with_sentence(self, sentence):
        self.config.readfp(open(self.filename))
        try:
            command = self.config.get("Commands", sentence)
        except ConfigParser.NoOptionError:
            print "No Command Found!!"
            return

        self._execute_command(command)

    def _execute_command(self, command):
        os.system(command)