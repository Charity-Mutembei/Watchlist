from email import message
from flask import render_template
from app import app

#views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    message = 'Hello World'
    return render_template('index.html', message = message)

def index():
    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home- Welcome to the best movie review website online'

    return render_template('index.html', title = title)
#movie route function
#below, te part in angle brackets is dynamic and it gives the part a movie.html file feel/reaction
@app.route('/movies/<int:movies_id>')
def movies(movies_id):
    '''
    View movies page function that returns the movie details page and its data
    '''
    return render_template('movies.html', id = movies_id)