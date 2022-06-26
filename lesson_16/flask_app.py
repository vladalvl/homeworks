from flask import Flask, render_template

app: Flask = Flask('lesson_16.flask_app', static_folder='static', template_folder='templates')


@app.route('/')
def foods():
    foods_ = 'Еда'
    return render_template('1.html', text=foods_)


@app.route('/books')
def books():
    type_of_books = ['Художественная литература', 'Детективы', 'Научно-популярная литература']
    return render_template('2.html', books=type_of_books)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
