from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Renderiza el archivo index.html

@app.route('/love-letter')  # Ruta para acceder a love letter
def love_letter():
    return render_template('love_letter.html')  # Asegúrate de que este archivo esté en templates

@app.route('/light_reveal_txt')
def light_reveal_txt():
    return render_template('light_reveal_txt.html')

if __name__ == '__main__':
    app.run(debug=True)
