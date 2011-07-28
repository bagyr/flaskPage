from flask import Flask, render_template
import markovChainGenerator as mark

chain = mark.LetterChain()
chain.fromJson('/root/src/page/markovChainGenerator/kapitan.json')
generator = mark.MarkovGenerator(chain, ' ')
app = Flask(__name__)

@app.route('/')

def hello_world(name = 'Kill Me.'):
    name = generator.makeSequence(20)
    return render_template('page.html', name=name)

if __name__ == '__main__':
    app.debug = False 
    app.run(host='0.0.0.0')

