#!/usr/bin/python3
'''start flask'''
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    '''Displays 'Hello HBNB!'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''Displays HBNB!'''
    return 'HBNB!'


@app.route('/c/<text>', strict_slashes=False)
def display_c_text(text):
    '''replace underscore with space'''
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route("/python", strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python_text(text='is cool'):
    '''replace underscore with space'''
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    '''display "n is a number" only if n is an integer'''
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_number_template(n):
    '''dispalys an HTML page with H1 tag: "Number: n" if n is an integer'''
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def display_number_odd_or_even(n):
    '''
    dispalys an HTML page with H1 tag: "Number:
    n is even|odd" if n is an integer
    '''
    even_or_odd = 'even' if n % 2 == 0 else 'odd'
    return render_template('6-number_odd_or_even.html',
                           number=n, even_or_odd=even_or_odd)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
