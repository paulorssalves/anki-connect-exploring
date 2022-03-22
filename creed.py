from toolset import (get_examples, get_frequency, 
                    get_text, get_tokens)
from words import Word, fetch_group_as_string                
import re

creed, wf = get_text("credo.txt")

tokens, token_set, phrases = get_tokens(creed)
frequency = get_frequency(tokens)

re.split(r'[.,]', creed)

wordlist = []
for pair in frequency:
    token = pair[0]
    wordlist.append(token)

fwl = ["ὁρατῶν", "ἀοράτων", "μονογενῆ", "φωτός", "ἀληθινὸν","ἀθιληθινοῦ", "ποιηθέντα", "ὁμοούσιον", "ἐγένετο", "ἡμετέραν", "σωτηρίαν", "κατελθόντα", "σαρκωθέντα", "Παρθένου",  "ἐνανθρωπήσαντα",  'Σταυρωθέντα', 'παθόντα', 'ταφέντα', 'ἀναστάντα', 'τρίτῃ', 'Γραφάς', 'ἀνελθόντα', 'καθεζόμενον', 'πάλιν', 'ἐρχόμενον', 'δόξης', 'κρῖναι', 'ζῶντας','νεκρούς','οὐκ','ἔσται', 'ζωοποιόν','ἐκπορευόμενον', 'σὺν', 'συμπροσκυνούμενον', 'συνδοξαζόμενον','λαλῆσαν','Προφητῶν','μίαν','καθολικὴν', 'ἀποστολικὴν','Ἐκκλησίαν','Ὁμολογῶ','βάπτισμα', 'ἄφεσιν', 'Προσδοκῶ', 'μέλλοντος','ζωὴν','γεννηθέντα']

examples = []
for word in fwl:
    examples.append(fetch_group_as_string(get_examples(word, phrases), single_list=True))

groups = zip(fwl, examples)

for group in groups:
    print(group)