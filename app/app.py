from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/')
def index():
    cursos = ['PHP', 'Python', 'Java', 'Kotlin', 'Dart', 'JavaScript']
    data={
        'titulo': 'Index123',
        'bienvenida': 'Saludos',
        'cursos': cursos,
        'numero_cursos': len(cursos)
    }
    return render_template('index.html', data=data)

@app.route('/contacto/<nombre>/<int:edad>')
def contacto(nombre, edad):
    data={
        'titulo': 'Contacto',
        'nombre': nombre,
        'edad': edad
    }
    return render_template('contacto.html', data=data)

def query_string():
    print(request)
    print(request.args)
    print(request.args.get('param1'))
    print(request.args.get('param2'))
    return 'ok'


if __name__ == '__main__':
    app.add_url_rule('/query_string', view_func=query_string)
    app.run(debug=True, port=5000)

