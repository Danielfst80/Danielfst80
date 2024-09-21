from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '¡Hola, este es el Bot de Salva Terra y Della Terra Educación!'

@app.route('/bot', methods=['POST'])
def bot_response():
    incoming_msg = request.values.get('Body', '').lower()
    response = ""
    
    if 'hola' in incoming_msg:
        response = "¡Hola! ¿Cómo te puedo ayudar hoy?"
    else:
        response = "Lo siento, no entiendo eso."
    
    return response

if __name__ == '__main__':
    app.run(debug=True)
    