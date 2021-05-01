from flask import Flask, render_template, current_app, request as app
from flask_apscheduler import APScheduler

app = Flask(__name__)

scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()
 
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/send', methods=['GET','POST'])
def sent():
    #get posteed form data using names assigned in HTML
    task = request.form['fname']
    deadline = request.form['deadline']
    #connect to database and insert task and deadline
    conn = sqlite3.connect('./static/data/senseDisplay.db')
    curs = conn.cursor()
    curs.execute("INSERT INTO tasklist (task, deadline, status) VALUES((?),(?),(?))", (task, deadline, "unstarted"))
    conn.commit()
    #close database connection
    conn.close()
    #render template with success message
    return render_template('sent.html', task=task, deadline=deadline)



'''
@app.route('/show')
def all():
    #CONNECT TO db
    conn = sqlite3.connect('./static/data/tasks.db')
    curs = conn.cursor()
    tasklist = []
    rows = curs.execute("SELECT * from todos")
    for row in rows:
        task = {'name': row[0], 'deadline':row[1], 'status':row[2]}
        tasklist.append(task)
    conn.close()
    return  render_template('index.html', tasklist=tasklist)
'''


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
