from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gerar_noticia', methods=['POST'])
def gerar_noticia():
    tema = request.form.get('tema')
    
    noticia = f"Em 2050, o mundo testemunha um avanço revolucionário em {tema}. Especialistas afirmam que essa mudança impactará a sociedade de maneiras inimagináveis."

    return render_template('noticia.html', noticia=noticia)

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

if __name__ == '__main__':
    app.run(debug=True)