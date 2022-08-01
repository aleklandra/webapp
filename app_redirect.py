from flask import Flask
from flask import render_template, request, redirect

from vsearch import search_for_letters

app = Flask(__name__)

@app.route('/')

def hello() -> '302':
    return redirect('/entry')
    
@app.route('/search', methods=['POST'])

def do_search() -> str:
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here your results'
    results = str(search_for_letters(phrase, letters))
    return render_template('result.html', the_title=title, the_results = results, the_phrase = phrase, the_letters = letters,)

    
@app.route('/entry')
    
def entry_page()-> 'html':
    return render_template('entry.html', the_title='Welcom to my web-app!')



app.run(debug=True)
