from bottle import route, run

@route('/', method='GET')
def index():
    return '''
    <form action="/" method="post">
       Username: <input name="Username" type="text" />
       Password: <input password="password" type="text" />
       <input value="Login" type="submit" />
    </form>'''


run(port=8080)    
