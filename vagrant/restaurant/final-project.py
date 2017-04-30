from flask import Flask, render_template, url_for, request, redirect, jsonify, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

app = Flask(__name__)

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Making an API endpoint (get request)
@app.route('/restaurants/JSON')
def restaurantsJSON():
	restaurants = session.query(Restaurant).all()
	return jsonify(Restaurant=[restaurant.serialize for restaurant in restaurants])

@app.route('/restaurant/<int:restaurant_id>/menu/JSON')
def restaurantMenuJSON(restaurant_id):
	restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
	items = session.query(MenuItem).filter_by(restaurant=restaurant).all()
	return jsonify(MenuItems=[item.serialize for item in items])

@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_item_id>/JSON')
def menuItem(restaurant_id, menu_item_id):
	item = session.query(MenuItem).filter_by(restaurant_id=restaurant_id, id=menu_item_id).one()
	return jsonify(MenuItem=item.serialize)

@app.route('/')
@app.route('/restaurants')
def showRestaurants():
	restaurants = session.query(Restaurant).all()
	return render_template('restaurants.html', restaurants=restaurants)


@app.route('/restaurant/new', methods=['GET', 'POST'])
def newRestaurant():
	if request.method == 'GET':
		return render_template('new-restaurant.html')
	elif request.method == 'POST':
		new_restaurant = Restaurant(name = (request.form['restaurant']))
		session.add(new_restaurant)
		session.commit()
		flash('New Restaurant Created')
		return redirect(url_for('showRestaurants'))
	

@app.route('/restaurant/<int:restaurant_id>/edit', methods=['GET', 'POST'])
def editRestaurant(restaurant_id):
	restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
	if request.method == 'GET':
		return render_template('edit-restaurant.html', restaurant=restaurant)
	elif request.method == 'POST':
		restaurant.name = request.form['restaurant']
		session.commit()
		return redirect(url_for('showRestaurants'))


@app.route('/restaurant/<int:restaurant_id>/delete', methods=['GET', 'POST'])
def deleteRestaurant(restaurant_id):
	restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
	if request.method == 'GET':
		return render_template('delete-restaurant.html', restaurant=restaurant)
	elif request.method == 'POST':
		session.delete(restaurant)
		session.commit()
		return redirect(url_for('showRestaurants'))


@app.route('/restaurant/<int:restaurant_id>/menu')
def showMenu(restaurant_id):
	restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
	items = session.query(MenuItem).filter_by(restaurant=restaurant).all()
	return render_template('menu.html', restaurant=restaurant, items=items)


@app.route('/restaurant/<int:restaurant_id>/menu/new', methods=['GET', 'POST'])
def newMenuItem(restaurant_id):
	restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
	if request.method == 'GET':
		return render_template('new-menu-item.html', restaurant=restaurant)
	elif request.method == 'POST':
		new_item = MenuItem(name = request.form['item'], price=request.form['price'], description=request.form['description'] ,restaurant_id=restaurant_id)
		session.add(new_item)
		session.commit()
		return redirect(url_for('showMenu', restaurant_id=restaurant_id))


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_item_id>/edit', methods=['GET', 'POST'])
def editMenuItem(restaurant_id, menu_item_id):
	item = session.query(MenuItem).filter_by(restaurant_id=restaurant_id, id=menu_item_id).one()
	if request.method == 'GET':
		return render_template('edit-menu-item.html', item=item)
	elif request.method == 'POST':
		item.name = request.form['item']
		session.commit()
		return redirect(url_for('showMenu', restaurant_id=restaurant_id))


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_item_id>/delete', methods=['GET', 'POST'])
def deleteMenuItem(restaurant_id, menu_item_id):
	item = session.query(MenuItem).filter_by(restaurant_id=restaurant_id, id=menu_item_id).one()
	if request.method == 'GET':
		return render_template('delete-menu-item.html', item=item)
	elif request.method == 'POST':
		session.delete(item)
		session.commit()
		return redirect(url_for('showMenu', restaurant_id=restaurant_id))

if __name__ == '__main__':
	app.debug = True
	app.run(host = '0.0.0.0', port = 5000)