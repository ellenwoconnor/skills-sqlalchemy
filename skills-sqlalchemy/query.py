"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Start here.


# Part 2: Write queries

# Get the brand with the **id** of 8.

Brand.query.filter_by(id=8).one()

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.

Model.query.filter(Model.name == "Corvette", Model.brand_name == 'Chevrolet').all()

# Get all models that are older than 1960.

Model.query.filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.

Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".

Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands with that were founded in 1903 and that are not yet discontinued.

Brand.query.filter(Brand.founded == 1903, Brand.discontinued == None).all()

# Get all brands with that are either discontinued or founded before 1950.

Brand.query.filter((Brand.discontinued == None) | (Brand.founded < 1950)).all()

# Get any model whose brand_name is not Chevrolet.

Model.query.filter(Model.brand_name != 'Chevrolet').all()

# Fill in the following functions. (See directions for more info.)


def get_model_info(year):

    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    model_info = db.session.query(Model.name, Model.brand_name, Brand.headquarters).join(Brand).filter(Model.year == year).all()

    for model in model_info:
        print model[1], model[0] + ". Headquarters: ", model[2]


def get_brands_summary():

    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    brands_models = {}

    brands = db.session.query(Model.brand_name, Model.name).all()

    for brand in brands:
        # If the brand is not listed in the dictionary, add it and include
        # the model as the key.
        if brand[0] not in brands_models:
            brands_models[brand[0]] = [brand[1]]

        # Otherwise, the brand is in the dictionary. If the value is not
        # already listed, append it.
        elif brand[1] not in brands_models[brand[0]]:
            brands_models[brand[0]].append(brand[1])

    for brand in brands_models:
        print "Brand: ", brand
        print "Models: ", ", ".join(brands_models[brand])
        print '\n'


# -------------------------------------------------------------------


# Part 2.5: Advanced and Optional

def search_brands_by_name(mystr):

    """Returns a list of objects that are brands whose name contains or
    is equal to the input string"""

    brand_objects = Brand.query.filter(Brand.name.like("%mystr%")).all()

    return brand_objects


def get_models_between(start_year, end_year):

    """Returns a list of objects that are models with years that fall
    between the start year and end year"""

    model_info = Model.query.filter(year > start_year, year < end_year).all()

    return model_info

# -------------------------------------------------------------------

# Part 3: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?

# This returns an query for a row of data where the value for the
# "name" field is Ford. Without adding .all() or .one() it is not yet 
# a data object.  

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?

# I think an association table is like 'BookGenre' - it manages a many-to-many
# mapping between two tables x,y by creating an intermediate table z 
# such that x is in a one-to-many relationship with z and y is in a one-to-many 
# relationship with z  
