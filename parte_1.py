from bottle import run, route

@route('/')
def index():
    return '<h1>hi live</h1>'

@route('/<person>')
def index(person):
    if person == 'charles':
        return 'welcome'
    return '<h1>hi {}</h1>'.format(person)

run(port=8080)
