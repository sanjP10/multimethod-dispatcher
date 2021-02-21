"""
Unit tests for dispatcher
"""
import unittest
from tests.functions import area, get_name, Person


class MultiMethodUnitTest(unittest.TestCase):
    """ Unit tests for dispatcher method"""

    def test_dispatcher_key(self):
        """Test dispatcher returns expected calculation type"""
        self.assertEqual(area({'type': 'circle', 'radius': 0.5}), 0.7853975)
        self.assertEqual(area({'type': 'rectangle', 'width': 5, 'height': 8}), 40)
        with self.assertRaises(Exception):
            area({'type': 'rhombus'})

    def test_dispatcher_key_on_type(self):
        """Test dispatcher returns expected calculation type"""
        person = Person('Steve', '2019-06-01')
        self.assertEqual(get_name(person), 'Steve is born on 2019-06-01')
        self.assertEqual(get_name({'name': 'Tom', 'dob': '2019-06-01'}),
                         'Tom is born on 2019-06-01')
        self.assertEqual(get_name('George', '2019-06-01'), 'George is born on 2019-06-01')
        self.assertEqual(get_name(2), "No name")
