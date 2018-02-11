import flask

app = flask.Flask(__name__)

# define route


@app.route('/')
def index():
    return '<h1> Holi </h1>'

# add a section
@app.route('/recursos')
def recursos_get():
    return '<h1> Seccion Recursos </h1>'

# this allows arguments input
@app.route('/recursos/<recurso_id>')
def recurso_id_get(recurso_id):
    return 'Estas ejecutando el servicio id: {}'.format(recurso_id)


if __name__ == '__main__':
    app.run(port=8080)
