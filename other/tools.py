from reverso_api import Client
from wiktionaryparser import WiktionaryParser
import itertools as itt
from words import Word
import pandas as pd

INPUT_LANGUAGE="ru", "Russian"
OUTPUT_LANGUAGE="en", "English"

client = Client(INPUT_LANGUAGE[0], OUTPUT_LANGUAGE[0])

def get_translations(word, example_number):
    translation_list = list(client.get_translations(word, 
    source_lang=INPUT_LANGUAGE[0], target_lang=OUTPUT_LANGUAGE[0]))[:example_number]
    return translation_list

def get_phrases_from_word(word, example_number, 
    group_languages=True):

    phrase_list = list(itt.islice(client.get_translation_samples(word, cleanup=True, 
    source_lang=INPUT_LANGUAGE[0], 
    target_lang=OUTPUT_LANGUAGE[0]), example_number))

    if group_languages is True:
        input_language_example_list = []
        output_language_example_list = []
        for group in phrase_list:
            input_language_example_list.append(group[0])
            output_language_example_list.append(group[1])
        
        phrase_dict = {"input phrases": input_language_example_list,
                       "output phrases": output_language_example_list}

        return phrase_dict
    else:
        return phrase_list

def get_word_data(word, translation_number, example_number):
    translations = get_translations(word, translation_number)
    if translations == []:
        return False
    else: 
        data =  {
            "name": word,
            "translations": translations, 
            "examples": get_phrases_from_word(word, example_number) 
            } 
        return data

def get_word_fallback(word):
    """
    No caso de a palavra não ser encontrada no Context Reverso
    Pelo menos pode-se tentar encontrar alguma palavra
    relacionada mais comum no Wiktionary, e daí
    produzir uma lista de repescagem.
    """
    word = Word(word)
    word_data = {
        "name": word.name,
        "data": word.get_text()[0][0],
        "definitions": [item for item in word.get_text()[0][1:]]
    }
    return word_data

def fetch_element_as_string(dict, element):
    """
    Transforma lista dentro do dicionário em string.
    Deste modo, o arquivo .csv final não fica cheio
    de colchetes.
    """
    if element == "name":
        return dict["name"]
    elif element == "translations":
        output = "" 
        for index in range(len(dict[element])):
            output += dict[element][index]
            if index < len(dict[element]) - 1:
                output+="\n\n"
        return output
    elif (element == "input phrases") or (element == "output phrases"):
        output = ""
        for index in range(len(dict["examples"][element])):
            output += dict["examples"][element][index]
            if index < len(dict["examples"][element]) - 1:
                output+="\n\n"
        return output
    else:
        return "Não há tal elemento."

def produce_dataframe(dict):
    data = dict
    final_dictionary = {
        "name": fetch_element_as_string(data, "name"),
        "traduções": fetch_element_as_string(data, "translations"),
        "exemplos": fetch_element_as_string(data, "input phrases"),
        "exemplos traduzidos": fetch_element_as_string(data, "output phrases"),
    }

    return pd.DataFrame(final_dictionary, index=[0])


def append_to_csv(DataFrame, OUTPUT_FILE_NAME):
    DataFrame.to_csv(OUTPUT_FILE_NAME, encoding="utf-8", mode="a", header=False, index=False)