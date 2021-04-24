from flask_apscheduler import flask_apscheduler

app = Flask(__name__)

scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()
 
@app.route('/')
def index():
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



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
