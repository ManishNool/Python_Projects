from flask import Flask, render_template, request

app = Flask(__name__)

def process_paragraph(paragraph):
    words = paragraph.split()
    word_count = len(words)
    word_details = {}

    for idx, word in enumerate(words):
        if word not in word_details:
            word_details[word] = [idx, 1]
        else:
            word_details[word][1] += 1

    return word_count, word_details

@app.route('/', methods=['GET', 'POST'])
def index():
    word_count = None
    word_details = None

    if request.method == 'POST':
        paragraph = request.form['paragraph']
        word_count, word_details = process_paragraph(paragraph)

    return render_template('index.html', word_count=word_count, word_details=word_details)

if __name__ == '__main__':
    app.run(debug=True, host = '0.0.0.0', port ='8010')






