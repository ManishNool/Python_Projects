import pickle 
import shelve

from flask import Flask, render_template, request

app = Flask(__name__)

def process_paragraph(paragraph):
    words = paragraph.split()
    word_counts = []
    for i, word in enumerate(words):
        count = words.count(word)
        if (word, i, count) not in word_counts:
            word_counts.append((word, i, count))
    total_words = len(words)

    with open('textanalyzerold.pkl', 'wb') as f:
        pickle.dump(word_counts, f)

    with shelve.open('textanalyzerold_shelve') as shelf:
        shelf['data'] = word_counts

    return total_words, word_counts

@app.route('/textanalyzerold', methods=['GET', 'POST'])
def word_counter():
    if request.method == 'POST':
        paragraph = request.form['paragraph']
        total_words, word_counts = process_paragraph(paragraph)
        return render_template('index.html', paragraph=paragraph, total_words=total_words, word_counts=word_counts)
    return render_template('index.html')

@app.route('/textanalyzerold_pkl', methods=['GET'])
def textanalyzerold_pkl_data():
    with open('textanalyzerold.pkl', 'rb') as f:
        loaded_data = pickle.load(f)
    return render_template('view_data.html', data=loaded_data)

@app.route('/textanalyzerold_shelve', methods=['GET'])
def textanalyzerold_data():
    with shelve.open('textanalyzerold_shelve') as shelf:
        loaded_data = shelf['data']
    return render_template('view_data.html', data=loaded_data)

def process_paragraph1(paragraph):
    words1 = paragraph.split()
    word_details = []
    word_details = [(v, i, words1.index(v), words1.count(v)) for i, v in enumerate(words1)]
    
    with open('textanalyzernew.pkl', 'wb') as f:
        pickle.dump(word_details, f)

    with shelve.open('textanalyzernew_shelve') as shelf:
        shelf['data'] = word_details

    return(word_details)

@app.route('/textanalyzernew', methods=['GET', 'POST'])
def word_counter1():
    if request.method == 'POST':
        paragraph = request.form['paragraph']
        word_details = process_paragraph1(paragraph)
        return render_template('index.html', paragraph=paragraph, word_details=word_details)
    return render_template('index.html')

@app.route('/textanalyzernew_pkl', methods=['GET'])
def textanalyzernew_pkl_data():
    with open('textanalyzernew.pkl', 'rb') as f:
        loaded_data1 = pickle.load(f)
    return render_template('view_data.html', data1=loaded_data1)

@app.route('/textanalyzernew_shelve', methods=['GET'])
def textanalyzernew_data():
    with shelve.open('textanalyzernew_shelve') as shelf:
        loaded_data1 = shelf['data']
    return render_template('view_data.html', data1=loaded_data1)

if __name__ == '__main__':
    app.run(debug=True, host = '0.0.0.0', port='8010')
