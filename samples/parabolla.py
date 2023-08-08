import csv, spacy

content = None

nlp = spacy.load("en_core_web_sm")

with open("sample_paragraphs.csv", 'r') as f:
    csvreader = csv.reader(f)
    content = [row for row in csvreader]

todd = content[2]
doc = nlp(todd)
sents = [sent for sent in doc.sents]

class Word:
    def __init__ (self, word, sentence):
        self.sentence = sentence
        self.word = word
        self.index = self.word.i

    def __repr__(self):
        return self.word.text

    def get_left():
        # TODO
        # garantir que funcione quando o número de palavras antes de self.word seja menor do que 6
        ## idem para o número de palavras após
        ## fazer desconsiderar as vírgulas e ponto e vírgula. Parar em ponto final.
        self.left = [token for token in self.sentence[self.index-6:self.index-1]]

    def get_right():
        # TODO 
        # idem ao método acima
        self.right = [token for token in self.sentence[self.index+1:self.index+6]]

class Sentence():
    def __init__ (self, sentence):
        self.sentence = sentence
        self.words = [Word(token, self.sentence) for token in self.sentence]

    def __repr__(self):
        return self.sentence.text

sl = [Sentence(sent) for sent in sents]
