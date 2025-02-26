from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///noticias.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Noticia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tema = db.Column(db.String(100), nullable=False)
    conteudo = db.Column(db.Text, nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gerar_noticia', methods=['POST'])
def gerar_noticia():
    tema = request.form.get('tema')
    conteudo = f"Em 2050, o mundo testemunha um avanço revolucionário em {tema}. Especialistas afirmam que essa mudança impactará a sociedade de maneiras inimagináveis."
    
    nova_noticia = Noticia(tema=tema, conteudo=conteudo)
    db.session.add(nova_noticia)
    db.session.commit()
    
    return render_template('noticia.html', noticia=conteudo)

@app.route('/noticias')
def listar_noticias():
    noticias = Noticia.query.all()
    return render_template('lista_noticias.html', noticias=noticias)

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)