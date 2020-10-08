from flask import Flask, request, render_template
from text_similarity import measure_similarity


app = Flask(__name__)

@app.route('/')
def entry_page():
    return render_template('index.html')

@app.route('/text_compare/', methods=['POST'])
def render_score():
    text1 = request.form['text1']
    text2 = request.form['text2']

    score = measure_similarity(text1,text2)

    return render_template('index.html', score=score, text1=text1, text2=text2)

if __name__ == '__main__':
    app.run(debug=True)