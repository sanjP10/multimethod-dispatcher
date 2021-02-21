
"""
Test functions for dispatcher
"""
from datetime import datetime
from multimethod import method, multi

@multi
def area(shape):
    """Multimethod dispatch key"""
    return shape.get('type')


@method(area, 'rectangle')
def area(square):
    """Get area of a rectangle"""
    return square.get('width') * square.get('height')


@method(area, 'circle')
def area(circle):
    """Get area of a circle"""
    return circle.get('radius') ** 2 * 3.14159


@method(area)
def area(unknown_shape):
    """Default for getting area"""
    raise Exception("Can't calculate the area of this shape")


class Person:
    """Person object to hold name and dob"""
    def __init__(self, name, dob):
        self.name = name
        self.dob = datetime.strptime(dob, '%Y-%m-%d')

    def get_name(self):
        """Return name"""
        return self.name

    def get_dob_as_str(self):
        """Return dob as string"""
        return self.dob.strftime('%Y-%m-%d')

@multi
def get_name(obj, _=None):
    """Multimethod dispatch key"""
    return obj.__class__


@method(get_name, dict)
def get_name(obj, _=None):
    """Dictionary function for getting name and dob from dict"""
    return "{} is born on {}".format(obj.get('name'), obj.get('dob'))


@method(get_name, str)
def get_name(obj, dob):
    """Dictionary function for getting name and dob from string"""
    return "{} is born on {}".format(obj, dob)


@method(get_name, Person)
def get_name(obj, _=None):
    """Person object type for getting name and dob"""
    return "{} is born on {}".format(obj.get_name(), obj.get_dob_as_str())


@method(get_name)  # Default
def get_name(*args, **kwargs):  # pylint: disable=W0613
    """Default response for any other object type"""
    return "No name"
