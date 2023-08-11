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
    return total_words, word_counts

@app.route('/textanalyzer', methods=['GET', 'POST'])
def word_counter():
    if request.method == 'POST':
        paragraph = request.form['paragraph']
        total_words, word_counts = process_paragraph(paragraph)
        return render_template('index.html', paragraph=paragraph, total_words=total_words, word_counts=word_counts)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host = '0.0.0.0', port='8010')
