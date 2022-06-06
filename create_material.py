import re, os, string, sys
import pandas as pd
import json, time, urllib.request
from tools.tokenization import (get_examples, get_frequency,
                    get_text, get_tokens)
from requests.exceptions import MissingSchema

from cltk import NLP
from cltk.lemmatize.grc import GreekBackoffLemmatizer
from cltk.alphabet.text_normalization import cltk_normalize

from tools.wordstruct import Word as WikWord
from tools.scraper import Word as BibleWord
from tools.scraper import (get_link, get_entry_soup, 
                            get_word_data, 
                            fetch_group_as_string, BASE_URL)

from urllib.error import URLError

def boldify_selected_word(word, string):
    string_l = string.split()
    for index in range(len(string_l)):
        if string_l[index] == word:
            bold = "<b>"+word+"</b>"
            string_l[index] = bold 
    return string_l, bold

def get_context_and_clean_up(word, concordance):

    # get word context from concordance
    c = concordance.concordance_list(cltk_normalize(word))

    # split string and make chosen word bold
    line, bold_word = boldify_selected_word(cltk_normalize(word), c[0][6])
    word_list = line

    # remove first and last words of string, as they are sometimes incomplete
    # and assert that the first and last 
    if word_list[0] not in (word, bold_word):
        del word_list[0]
        if word_list[0] in string.punctuation:
            del word_list[0] 
    if word_list[len(word_list) - 1] not in (word, bold_word):
        del word_list[len(word_list) - 1]

    # get string with extra spaces
    unfinished_string = " ".join(word_list)
    
    # remove unnecessary spaces from string
    trailing_spaces_start = r"^\s+"
    trailing_spaces_end = r"\s+$"

    cleaned_up_pre = re.sub(r'\s([?.!,:;"](?:\s|$))', r'\1', unfinished_string)
    cleaned_up_start = re.sub(trailing_spaces_start, "", cleaned_up_pre)
    final_string = re.sub(trailing_spaces_end, "", cleaned_up_start)
    
    return final_string

def clean_up(string):
    trailing_spaces_start = r"^\s+"
    trailing_spaces_end = r"\s+$"

    cleaned_up_pre = re.sub(r'([?.!,:;"](?:\s|$))', "", string.split()[0])
    cleaned_up_start = re.sub(trailing_spaces_start, "", cleaned_up_pre)
    cleaned_up = re.sub(trailing_spaces_end, "", cleaned_up_start)

    return cleaned_up

def request(action, **params):
    return {'action': action,
            'params': params,
            'version': 6}

def invoke(action, **params):
    requestJson = json.dumps(request(action, **params)).encode('utf-8')
    response = json.load(urllib.request.urlopen(urllib.request.Request('http://localhost:8765', requestJson)))

    if len(response) != 2:
        raise Exception('response has an unexpected number of fields')

    if 'error' not in response:
        raise Exception('response is missing required error field')
    
    if 'result' not in response:
        raise Exception('response is missing required result field')

    if response['error'] is not None:
        raise Exception(response['error'])

    return response['result']

def get_input_for_material(wordlist, anki_cards):

    notes = []
    for card in anki_cards:
        notes.append(cltk_normalize(clean_up(card['fields']['Word']['value'])))

    fwl = [cltk_normalize(word) for word in wordlist if word not in notes]
    notes_group = lemmatizer.lemmatize(notes)
    fwl_group = lemmatizer.lemmatize(fwl)
    notes_lemmas = set([tuple[1] for tuple in notes_group])
    fwl_lemmas = set([tuple[1] for tuple in fwl_group])

    filtered_fwl_lemmas = [word for word in fwl_lemmas if word not in notes_lemmas]
    reworked_fwl = [tuple for tuple in fwl_group if tuple[1] in filtered_fwl_lemmas]

    for i in range(len(reworked_fwl)):
        if reworked_fwl[i][0] == reworked_fwl[i][1]:
            reworked_fwl[i] = reworked_fwl[i][0]

    return reworked_fwl

def fetch_bible_word(word):
    link = get_link(BASE_URL, word)
    soup = get_entry_soup(link)
    word = BibleWord(get_word_data(soup))

    return word

def searcher(word):
    if type(word) == tuple:
        try:
            bible_word = fetch_bible_word(word[0])
            return {"search_num": 1, "source": "BibleHub", "input": word[0], "output": bible_word.data}

        except MissingSchema:
            try:
                bible_word = fetch_bible_word(word[1])
                return {"search_num": 2, "source": "BibleHub", "input": word[0], "output": bible_word.data}

            except MissingSchema:
                return {"search_num": 2, "source": None, "input": word[0], "output": None}

    elif type(word) == str:
        try: 
            bible_word = fetch_bible_word(word)
            return {"search_num": 1, "source": "BibleHub", "input": word, "output": bible_word.data}

        except:
                return {"search_num": 1, "source": None, "input": word, "output": None}
    else:
        return {"search_num": 0, "source": None, "input": word, "output": None}


def progress(count, total, suffix=''):
    # taken from Vladimir Ignatev, from GitHub gist https://gist.github.com/vladignatyev/06860ec2040cb497f0f3
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', suffix))
    sys.stdout.flush()  # As suggested by Rom Ruben

def time_log():
    DURATION = 60
    for second in range(DURATION):
        sys.stdout.write('Wait... %s/%s\r' % (second, DURATION))
        time.sleep(1)
        sys.stdout.flush()

def acquire_data(list, amount=None):

    RESPECTABLE_RANGE=10

    bible_searches = 0
    data = []
    blanks = []
    already_present = []

    if (amount != None) and (amount <= len(list)):
        number = range(amount)
    else:
        number = range(len(list))

    for index in number:

        word_dict = searcher(list[index])

        # print progress bar
        progress(index+1, len(number), " {} ({}/{})".format(word_dict["input"], index+1, len(number)))

        if word_dict["source"] != None:
            result = (word_dict["source"], word_dict["input"], word_dict["output"])
            if result[2] not in already_present:
                data.append(result)
            already_present.append(result[2])
        else:
            blanks.append(word_dict["input"])

        bible_searches += word_dict["search_num"]

        if bible_searches >= RESPECTABLE_RANGE:
            time_log()
            bible_searches = 0
    
    return data, blanks


def produce_material(output_file_name, data=None, blanks=None):
    if type(output_file_name) is not str:
        raise TypeError("variable 'output_file_name' must be of type 'str'.")

    if (data is not None) and (data != []):
        for item in data:
            if item[0] is not None:

                curr = item[2]
                concordances = curr["concordances"]

                dc = {
                    "word": clean_up(concordances["Original Word"]),
                    "phonetics": concordances["Phonetic Spelling"],
                    "category": concordances["Part of Speech"],
                    "meaning": concordances['Definition'],
                    "greek": fetch_group_as_string([tuple[0] for tuple in curr['examples']], single_list=True),
                    "english": fetch_group_as_string([tuple[1] for tuple in curr['examples']], single_list=True)
                }
                dc["context"] = "\""+get_context_and_clean_up(item[1], wf)+"\""
                dc["original"] = item[1]        
                dc["source"] = item[0]        
                # to display which word is being worked upon at the time

                words_dataframe = pd.DataFrame.from_dict(dc, orient="index")
                words_dataframe = words_dataframe.transpose()
                words_dataframe.to_csv(os.path.join("output", output_file_name+".csv"), 
                                                    encoding="utf-8", mode="a", 
                                                    header=False, index=False)
            
    if (blanks is not None) and (blanks != []):
        blanks_dataframe = pd.DataFrame(blanks)
        blanks_dataframe= blanks_dataframe.transpose()
        blanks_dataframe.to_csv(os.path.join("blanks", output_file_name+"_blanks.csv"), 
                                            encoding="utf-8", mode="a", 
                                            header=False, index=False)


if __name__ == "__main__":

    def get_number():
        try: 
            number = sys.argv[3]
            return number
        except IndexError:
            return None 

    print("Running lemmatizer...\n")
    lemmatizer = GreekBackoffLemmatizer()

    text, wf = get_text(os.path.join("textos", sys.argv[1] + ".txt"))
    
    tokens, token_set, phrases = get_tokens(text)
    frequency = get_frequency(tokens)
    cltk_nlp = NLP(language="grc")
    cltk_doc = cltk_nlp.analyze(text)

    wordlist = []

    for pair in frequency:
        token = pair[0]
        wordlist.append(token)

    try:
        noteIDs = invoke('findNotes', query="deck:"+sys.argv[2]) 
        notesInfo = invoke('notesInfo', notes=noteIDs)

        reworked_fwl = get_input_for_material(wordlist, notesInfo)
        print(reworked_fwl)

        print("\nGetting online data...\n")

        data, blanks = acquire_data(reworked_fwl, get_number())
        print()

        print("\nCreating material...")
        produce_material(sys.argv[1], data=data, blanks=blanks)
        regex_repair = re.compile("\"\"")

        print("\nRemoving safety quotation marks...\n")
        with open(os.path.join("output", sys.argv[1]+".csv")) as csv:
            for line in csv:
                regex_repair.sub("", line)

        print("\nDone.\n")

    except urllib.error.URLError as e:
        print("\nThe", e, "error occurred. You need to have an Anki instance open.")

