import json
from flask import Flask, request, render_template, jsonify
from text_similarity import measure_similarity, measure_similarity_multiple
import os


app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def entry_page():
    if request.method == 'POST':
        samples = json.loads(request.data)
    
        results = measure_similarity_multiple(samples)

        return jsonify(results)
    else:
        return render_template('index.html')

@app.route('/text_compare/', methods=['POST'])
def render_score():
    text1 = request.form['text1']
    text2 = request.form['text2']

    score = measure_similarity(text1,text2)

    if score == 'nan':
        message = 'Enter two text samples before a score can be given.'
        return render_template('index.html', message=message, text1=text1, text2=text2)
    else:
        return render_template('index.html', score=score, text1=text1, text2=text2)
        

if __name__ == '__main__':
    port = os.environ.get('PORT', 5000)
    app.run(port=port, debug=True, host='0.0.0.0')