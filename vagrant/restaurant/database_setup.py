import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

#The class is the table.The class inherits properties from sqlalchemy with the 'Base object'.
class Restaurant(Base):
	#The following line names the table
	__tablename__  = 'restaurant'
	
	#Here we create columns, using arguments that we imported on the top.
	name = Column(String(80), nullable=False)#this means that a row can't be created without this information
	id = Column(Integer, primary_key=True)

class MenuItem(Base):
	__tablename__ = 'menu_item'
	
	name = Column(String(80), nullable=False)
	id = Column(Integer, primary_key=True)
	course = Column(String(250))
	description = Column(String(250))
	price = Column(String(8))
	restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
	restaurant = relationship(Restaurant)

engine = create_engine('sqlite:///restaurantmenu.db')

Base.metadata.create_all(engine)
