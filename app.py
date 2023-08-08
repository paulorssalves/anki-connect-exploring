from tools.tools import (get_word_data, produce_dataframe,
                   append_to_csv, time_log, progress)
from flask import Flask, render_template, request, jsonify
from json import loads
import pandas as pd
import spacy

app = Flask(__name__)
nlp = spacy.load("en_core_web_sm")

class ProcessedContent():
    def __init__(self, content):
        self.content  = content
        self.nlp_base = nlp(self.content)
        self.token_list = [str(token) for token in self.nlp_base if not (token.is_punct or token.is_quote or token.is_bracket)] 
        self.lemmata = [token.lemma_ for token in self.nlp_base if not (token.is_punct or token.is_quote or token.is_bracket)] 

    def get_tokens(self):
        return self.token_list

    def get_lemmata(self):
        return self.lemmata

@app.route('/')
def index():
    if request.method == 'POST':
        user_text = request.form['input_content']
        content = ProcessedContent(user_text)
        return content.get_lemmata()
    return render_template('index.html')

@app.route('/connect', methods=['GET', 'POST'])
def anki_connect():
    if request.method == 'POST':
        user_text = request.form['input_content']
        content = ProcessedContent(user_text)
        return content.get_lemmata()
    return render_template('textarea.html')

@app.route('/context', methods=['GET', 'POST'])
def context():
    if request.method == 'POST':
        user_text = request.form['input_content'].splitlines()

        WAIT_TIME = 5
        TRANSLATION_NUMBER = 3
        EXAMPLE_NUMBER = 3
        REQUEST_NUMBER = len(user_text)

        output_df = pd.DataFrame() 
        for index in range(len(user_text)):
            word_data = get_word_data(user_text[index], TRANSLATION_NUMBER,
                                      EXAMPLE_NUMBER)
            if word_data == False:
                continue

            df = produce_dataframe(word_data)
            output_df = pd.concat([output_df, df])
            time_log(WAIT_TIME)
        
        csv_data = output_df.to_csv(index=False, header=False, encoding='utf-8')

        return jsonify(csv_data)

    return render_template('context.html')

if __name__ == '__main__':
    app.run(debug=True)
