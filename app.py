from flask import Flask
from flask import render_template, request, redirect, escape

from vsearch import search_for_letters
from datetime import datetime


app = Flask(__name__)

def log_requests(req: 'flask_request', res: str) -> None:
    now = datetime.now()
    with open('log_file.txt', 'a') as log_file:
        print(str(now),req.form, req.remote_addr, req.user_agent, res, file=log_file, sep='|')

@app.route('/')

def hello() -> '302':
    return redirect('/entry')

@app.route('/search', methods=['POST'])

def do_search() -> str:
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here your results'
    results = str(search_for_letters(phrase, letters))
    log_requests(request,results)
    return render_template('result.html', the_title=title, the_results = results, the_phrase = phrase, the_letters = letters,)
    
 
@app.route('/entry', methods=['POST','GET'])
    
def entry_page()-> 'html':
    log_requests(request,res='')
    return render_template('entry.html', the_title='Welcom to my web-app!')
    
@app.route('/logs', methods=['POST','GET'])

def log_page() -> 'html':
    content = []
    with open('log_file.txt') as log:
        for line in log:
            content.append([])
            for item in line.split('|'):
                content[-1].append(escape(item))
    titles = ('Date','Form Data', 'Remote_addr', 'User_agent', 'Results') 
    return render_template('logs.html', the_title = 'Here are logs of our web-app', the_row_titles=titles, the_data=content)

if __name__ == '__main__':
    app.run(debug=True)
