from flask import Flask, render_template, current_app as app
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    prompt="Leave an inspirational message!"
    return render_template('index.html', prompt=prompt)

@app.route('/all')
def all():
    #CONNECT TO db
    conn = sqlite3.connect('./static/data/senseDisplay.db')
    curs = conn.cursor()
    messages = []
    rows = curs.execute("SELECT * from messages")
    for row in rows:
        message = {'name': row[0], 'message':row[1]}
        messages.append(message)
    conn.close()
    return  render_template('all.html', messages=messages)

@app.route('/send', methods=['POST'])
def sent():
    #get posted form data using names assigned in
    message=request.form['message']
    name=request.form['name']
    #generate string to display on Sense HAT
    #display = message + " Love, " + name

    #connect to database and insert message and name
    conn = sqlite3.connect('./static/data/senseDisplay.db')
    curs = conn.cursor()
    curs.execute("INSERT INTO messages (name, message) VALUES((?),(?))", (name, message))
    conn.commit()
    #close dataase connection
    conn.close()
    #reset sensehat
    #sense.clear(255,255,255)

    #display message on Sense HAT
    #sense.show_message(display)

    #display success message to sending user
    return render_template('send.html', message=message, name=name)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
