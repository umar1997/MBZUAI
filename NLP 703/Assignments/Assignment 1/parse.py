# Regex Cheat Sheet
# https://learnbyexample.github.io/python-regex-cheatsheet/
# https://towardsdatascience.com/regex-cheat-sheet-python-3dd0c4b5b4c6

# CMU Pronouncing Dictionary
# http://www.speech.cs.cmu.edu/cgi-bin/cmudict


import sys
import re
import json


def readInput():
    N = len(sys.argv)
    NameOfScript = sys.argv[0]

    if N == 1:
        print("WARNING: No Input given.")
        return None
    elif N == 2:
        return sys.argv[1]

    else:
        print("WARNING: Too many inputs.")
        print("Script takes 1 string as input.")
        return None

class Parser:
    def __init__(self, inputSentence):
        self.inputSentence = inputSentence
        
        with open('words.json') as f:
            WORDS = json.load(f)
        self.WORDS = WORDS
        
        self.PHONEMES = {value:key for key, value in WORDS.items()}

    def parseInput(self,):
        x = self.inputSentence.upper().strip()
        wordList = x.split('.')

        formattedWords = []
        for x in wordList:
            x = re.sub(r'_', ' ', x)
            x = re.findall(r'\w+', x)
            x = ' '.join(x)
            formattedWords.append(x)
        return formattedWords

    def retrieveWord(self,):
        inputWordList = self.parseInput()
        
        output = []
        for w in inputWordList:
            try:
                output.append(self.PHONEMES[w])
            except:
                output.append('<UNK>')
                
        return ' '.join(output).upper()
    
    def run(self,):
        print(self.retrieveWord())
        
        
        

if __name__ == '__main__':
    inputSentence = readInput()
    # inputSentence = "/DH /IH/ S . /L/ AE   /NG - /G/ //W/ /AH/ JH .IH/__?Z/. G/// /OW/ {L D}"
    # inputSentence = "/DH /IH/ S . /L/ AE   /NG - /G/ //W/ /AH/ .IH/__?Z/. G/// /OW/ {L D}" 
    p = Parser(inputSentence)
    p.run()