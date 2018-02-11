import flask

app = flask.Flask(__name__)


def square(v1, v2):
    return v1 ** v2


def Sum(v1, v2):
    return v1 + v2


# ###
fun_handle = {'square': square, 'sum': Sum}


@app.route('/api/<api_id>')
def api_get(api_id):
    if 'v1' not in flask.request.args and 'v2' not in flask.request.args:
        return 'No value has been entered'
    else:
        # arguments go to server as strings
        v1 = int(flask.request.args['v1'])
        v2 = int(flask.request.args['v2'])

        return '{0}: {1}'.format(api_id, fun_handle[api_id](v1, v2))


if __name__ == '__main__':
    app.run(port=8080)
