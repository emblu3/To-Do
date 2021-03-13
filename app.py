from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta 
from flask_session import Session

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(80), nullable=False)
    priority = db.Column(db.String(2))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST': #grab task and put on database
        
        task_content = request.form['content'] #content of input
        task_priority = request.form.getlist('category')
        task_priority = task_priority[0]
        if task_priority == "Urgent":
            priority = 1
        elif task_priority == 'Important':
            priority = 2
        else:
            priority = 3
        new_task = Todo(content=task_content, category=task_priority, priority=priority) #create new task from input

        try: #commit task to database
            db.session.add(new_task)
            db.session.commit()

            return redirect('/') #redirect back home
        except:
            return 'There was an issue adding your task'

    else:
        tasks = Todo.query.order_by(Todo.priority).order_by(Todo.date_created).all() #return database contents in order of creation (new-old)
        return render_template('index.html', tasks=tasks)


@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that task'


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['content']
        
        task_priority = request.form.getlist('category')
        task_priority = task_priority[0]
        task.category = task_priority
        if task_priority == "Urgent":
            priority = 1
        elif task_priority == 'Important':
            priority = 2
        else:
            priority = 3
        task.priority = priority

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating your task'


if __name__ == '__main__':
    app.run(debug=False)
