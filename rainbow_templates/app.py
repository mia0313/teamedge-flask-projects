from flask import Flask, render_template, current_app as app

app = Flask(__name__)

@app.route('/')
def index():
    name = "Mia"
    return render_template('index.html', name=name)

@app.route('/red')
def red():
    colour="Red"
    return render_template('rainbow.html', colour=colour)

@app.route('/orange')
def orange():
    colour="Orange"
    return render_template('rainbow.html', colour=colour)

@app.route('/yellow')
def yellow():
    colour="Yellow"
    return render_template('rainbow.html', colour=colour)

@app.route('/green')
def green():
    colour="Green"
    return render_template('rainbow.html', colour=colour)

@app.route('/blue')
def blue():
    colour="Blue"
    return render_template('rainbow.html', colour=colour)

@app.route('/indigo')
def indigo():
    colour="Indigo"
    return render_template('rainbow.html', colour=colour)

@app.route('/violet')
def violet():
    colour="Violet"
    return render_template('rainbow.html', colour=colour)

@app.route('/rainbow')
def rainbow():
    colours=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    return render_template('links.html', colours=colours)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
