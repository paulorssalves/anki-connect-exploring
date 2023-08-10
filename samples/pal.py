import spacy

# nlp = spacy.load("en_core_web_sm")

class Word:
    """
    Classe com o intuito de facilitar a obtenção do contexto das palavras
    para produção de exemplos.
    """
    def __init__ (self, word, sentence):
        self.sentence = sentence
        self.word = word
        self.i = self.word.i

    def get_context(self, trim=True, trim_left=6, trim_right=6):
        """
        Obtém o contexto da palavra, exibindo `trim_left` palavras à esquerda
        e `trim_right` palavras à direita se `trim`==True
        """
        # alternativa: retornar a frase completa
        if trim==False:
            return self.sentence.text

        leftwards_feasible = self.i
        rightwards_feasible = len(self.sentence) - self.i

        # limita o valor de trim_left se não houver palavras o suficiente à esquerda
        if (leftwards_feasible < trim_left and leftwards_feasible >= 0):
            trim_left = self.i - leftwards_feasible

        # limita o valor de trim_right se não houver palavras o suficiente à direita 
        if (rightwards_feasible < trim_right and rightwards_feasible >= 0):
            trim_right = rightwards_feasible - 1

        self.trimmed = self.sentence[self.i-trim_left:1+self.i+trim_right].text

        return self.trimmed

    def __repr__(self):
        return self.word.text

class Sentence():
    """
    Classe elaborada para facilitar a vinculação entre palavras e frases
    """
    def __init__ (self, sentence):
        self.sentence = sentence
        
        # cada palavra já é deste modo contextualizada
        self.words = [Word(token, self.sentence) for token in self.sentence]

    def __repr__(self):
        return self.sentence.text
