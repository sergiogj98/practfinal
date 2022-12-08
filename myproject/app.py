from flask import Flask, render_template, request, redirect,request, escape
from search4web import search4letters, log_request
app = Flask(__name__)
@app.route('/')
def hello() -> '302':
    return redirect('/entry')

@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to search for letters on the web!')

@app.route('/search', methods=['POST'])
def do_search() -> str:
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are you results: '
    result = str(search4letters(phrase, letters))
    log_request(request, result)
    return render_template('results.html', the_title=title,the_phrase=phrase, the_letters=letters, the_results=result)

@app.route('/viewlog')
def view_the_log() -> str:
    with open('search.log', 'r') as log:
        contents = log.read()
        return escape(contents)

if __name__  == '__main__':
    app.run()

