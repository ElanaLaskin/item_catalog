from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

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
	app.run(host = '0.0.0.0', port = 5000)