"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise instructions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()


# -------------------------------------------------------------------
# Part 2: Discussion Questions


# 1. What is the datatype of the returned value of
# ``Brand.query.filter_by(name='Ford')``?

# An object (instantiation of Brand). However, if there were more than one
# car with the name of Ford, and if this query ended with .all(), there would
# be returned a list of objects.


# 2. In your own words, what is an association table, and what type of
# relationship (many to one, many to many, one to one, etc.) does an
# association table manage?

# An association table is the place of connection for two different tables.  
# These two different tables are associated to one another via many to many
# relationships.  If the two were to be directly associated to one another,
# there would be many duplicate rows between the two tables.  So, association
# tables allow one to take the primary key of each of the two different tables
# and make them foreign keys in the association table.  The association table 
# therefore manages many to one relationships, because there could be many 
# rows or instances (according to the db) in the association table
# associated with one row or instance of one of the different tables.  
# In the class lab exercise with ratings, there could be many ratings
# associated with a user and many ratings associated with a movie,
# but only one user could be associated with a rating, and only one movie
# could be associated with a rating.   



# -------------------------------------------------------------------
# Part 3: SQLAlchemy Queries


# Get the brand with the brand_id of ``ram``.
q1 = Brand.query.filter_by(brand_id='ram').first()

# Get all models with the name ``Corvette`` and the brand_id ``che``.
q2 = Model.query.filter(Model.name == 'Corvette', Model.brand_id == 'che').all()

# Get all models that are older than 1960.
q3 = Model.query.filter(Model.year > 1960).all()

# Get all brands that were founded after 1920.
q4 = Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with ``Cor``.
q5 =  Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.
q6 = Brand.query.filter(Brand.founded==1903, Brand.discontinued.is_(None)).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
q7 = Brand.query.filter((Brand.discontinued.isnot(None)) | (Brand.founded < 1950)).all()

# Get all models whose brand_id is not ``for``.
q8 =  q8 = Model.query.filter(Model.brand_id != 'for').all()


# -------------------------------------------------------------------
# Part 4: Write Functions


def get_model_info(year):
    """Takes in a year and prints out each model name, brand name, and brand
    headquarters for that year using only ONE database query."""

    q1 = db.session.query(Model.year, Brand.name, Brand.headquarters).join(Brand).filter(Model.year=year).all()
    return q1

def get_brands_summary():
    """Prints out each brand name (once) and all of that brand's models,
    including their year, using only ONE database query."""

    q2 = db.session.query(Brand.name, Model.name, Model.year).join(Model).all()
    return q2

def search_brands_by_name(mystr):
    """Returns all Brand objects corresponding to brands whose names include
    the given string."""

    q3 =  Brand.query.filter((Brand.name.like('%'+mystr+'%')) | (Brand.name == mystr)).all()
    return q3


def get_models_between(start_year, end_year):
    """Returns all Model objects corresponding to models made between
    start_year (inclusive) and end_year (exclusive)."""

    q4 = Model.query.filter(Model.year >= start_year, Model.year < end_year).all()
    

