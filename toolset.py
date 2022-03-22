from nltk import word_tokenize, sent_tokenize, FreqDist, Text

def get_text(file):
    f = open(file, "r", encoding="utf-8")
    text = f.read()
    tokens = word_tokenize(text)
    reworked_text = Text(tokens)

    return text, reworked_text

def get_tokens(text):
    negatives = [",", "'", ".", "’"]
    phrases = sent_tokenize(text)
    tokens = [word for word in word_tokenize(text) if word not in negatives]
    token_set = set(tokens)

    return tokens, token_set, phrases

def get_frequency(tokens):
    frequency = FreqDist(tokens)
    sorted_frequency_list = sorted(frequency.items(), key=lambda pair: pair[1])

    return sorted_frequency_list 

def get_examples(word, phrases):
    n = 0
    l = []
    for phrase in phrases:
        if word in phrase:
            if n <= 3:
                l.append(phrase)
                n+=1
            else:
                break
    return l