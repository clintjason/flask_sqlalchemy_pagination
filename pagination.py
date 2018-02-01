from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/jason/Projects/flask-sqlalchemy/pagination/pagination.db'
app.config['DEBUG'] = True
db = SQLAlchemy(app)

class Thread(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(50))

@app.route('/<int:page_num>')
@app.route('/')
def thread(page_num=None):
	if(page_num):
		threads = Thread.query.paginate(per_page=5, page=page_num, error_out=True)
		return render_template('index.html',threads=threads)
	else:
		threads = Thread.query.paginate(per_page=5, page=1, error_out=True)
		return render_template('index.html',threads=threads)

if __name__ == '__main__':
	app.run()

