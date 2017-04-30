import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

#The class is the table.The class inherits properties from sqlalchemy with the 'Base object'.
class Catagories(Base):
	#The following line names the table
	__tablename__  = 'catagories'
	
	#Here we create columns, using arguments that we imported on the top.
	name = Column(String(80), nullable=False)#this means that a row can't be created without this information
	id = Column(Integer, primary_key=True)

engine = create_engine('sqlite:///catalog.db')