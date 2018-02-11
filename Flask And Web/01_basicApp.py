from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/<user>')
def index(user=None):
    return render_template('user.html', user=user)


@app.route('/shopping')
def shopping():
    food = ['Cheese', 'Tuna', 'Beef']
    return render_template('shopping.html', food=food)


@app.route('/bacon', methods=['GET', 'POST'])
def bacon():
    if request.method == 'POST':
        return 'You are using POST'
    else:
        return 'You are probably using GET'


@app.route('/profile/<username>')
def profile(username):
    return render_template('profile.html', username=username)


@app.route('/post/<int:post_id>')
def post(post_id):
    return '<h2> Post ID: {}</h2>'.format(post_id)


if __name__ == '__main__':
    app.run(debug=True)
