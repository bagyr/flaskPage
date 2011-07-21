from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def hello_world(name = 'pasha'):
    return render_template('page.html', name=name)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')

