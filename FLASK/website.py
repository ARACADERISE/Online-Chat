from flask import Flask

app = Flask(__name__)

class FlaskWebApp:

    def __init__(self):pass # not needed

    @app.route('/')
    def _Show_Homepage_():
        return '<h1> HELLO </h1>'
    
    def RUN(self): app.run(debug=True)
