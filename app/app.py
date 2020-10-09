import json
from flask import Flask, request, render_template, jsonify
from text_similarity import measure_similarity, measure_similarity_multiple


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

@app.route('/api/', methods=['POST'])
def request_score():
    samples = json.loads(request.data)
    
    results = measure_similarity_multiple(samples)

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')