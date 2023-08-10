import csv, spacy, re

content = None
nlp = spacy.load("en_core_web_sm")

with open("sample_paragraphs.csv", 'r') as f:
    csvreader = csv.reader(f)
    content = [row for row in csvreader]

todd = content[2]
todd = todd[0]
doc = nlp(todd)
sents = [sent for sent in doc.sents]

class Word:
    def __init__ (self, word, sentence):
        self.sentence = sentence
        self.word = word
        self.i = self.word.i

    def __repr__(self):
        return self.word.text

    def get_left(self, nleft=6):
        # TODO
        # - [ ] fazer desconsiderar as vírgulas e ponto e vírgula. Parar em ponto final.
        lower_limit = 0 # self.i - self.i
        leftwards_feasible = self.i

        if (leftwards_feasible < nleft and leftwards_feasible > 0):
            self.left = [token.text for token in self.sentence[self.i-leftwards_feasible:self.i]]

        elif (leftwards_feasible >= nleft):
            self.left = [token.text for token in self.sentence[self.i-nleft:self.i]]

        elif (leftwares_feasible == 0 or nleft <= 0):
            self.left = ""

        return " ".join(self.left)

    def get_right(self, nright=6):
        # TODO 
        # - [ ] fazer desconsiderar as vírgulas e ponto e vírgula. Parar em ponto final.
        upper_limit = len(self.sentence) - self.i 
        rightwards_feasible = upper_limit
        take_right = nright+1

        if (rightwards_feasible < take_right and rightwards_feasible > 0):
            self.right = [token.text for token in self.sentence[self.i+1:self.i+rightwards_feasible]]

        elif (rightwards_feasible >= take_right):
            self.right = [token.text for token in self.sentence[self.i+1:self.i+take_right]]

        elif (rightwards_feasible == 0 or take_right <= 1):
            self.right = ""

        return " ".join(self.right)

    def get_context(self):
        pre_processor = r'\s([?.!",:;\'](?:\s|$))'
        raw_context = self.get_left() + " " + self.word.text + " " + self.get_right()
        context_phase01 =  re.sub(pre_processor, r'\1', raw_context)
        context = re.sub(r'\s’', "'", context_phase01)
        return context

class Sentence():
    def __init__ (self, sentence):
        self.sentence = sentence
        self.words = [Word(token, self.sentence) for token in self.sentence]

    def __repr__(self):
        return self.sentence.text

text = "This is an example sentence that we want to trim."

# Process the text
doc = nlp(text)

# Define the number of words to trim from the left and right
words_to_trim = 2

# Trim the sentence by eliminating words from both ends
trimmed_text = doc[words_to_trim:-words_to_trim].text

print("Original Sentence:", text)
print("Trimmed Sentence:", trimmed_text)
