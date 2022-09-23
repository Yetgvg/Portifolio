from flask import Flask,render_template,url_for

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/portifolio.html')
def portifolio():
    return render_template('portifolio.html')

@app.route('/informacao.html')
def informacao():
    return render_template('informacao.html')

if __name__ == "__main__":
    app.run(debug=True)