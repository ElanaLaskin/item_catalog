from flask import Flask, render_template
from database_setup import Base, Catagories, engine, DBSession

app = Flask(__name__)

session = DBSession()

@app.route('/')
def home():
	restaurants = session.query(Restaurant).all()
	return render_template('home.html', restaurants=restaurants)

@app.route('/<category>')
def show_category(category):
	return render_template('category.html', category=category)

@app.route('/<category>/<item>')
def show_item(category, item):
	return render_template('item.html', item=item)

@app.route('/<category>/<item>/edit')
def edit_item(category, item):
	return render_template('edit_item.html', item=item)

@app.route('/<category>/<item>/delete')
def delete_item(category, item):
	return render_template('delete_item.html', item=item)

if __name__ == '__main__':
	app.debug = True
	app.run(host = '0.0.0.0', port = 5001)