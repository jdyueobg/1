from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def sport():
    return render_template('index.html')

@app.route('/takafa')
def takafa():
    return render_template('takafa.html')

@app.route('/arabec')
def arabec():
    return render_template('arabec.html')
if __name__ == '__main__':
    app.run()