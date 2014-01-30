import unittest
import json
import pson
from  pson import pathquery as pq

class PsonTestCase(unittest.TestCase):
    def setUp(self):
        with open("testdata/ar00498-98342.json") as json_file:
            self.jsondata = json.load(json_file)


    def test_basic_query(self):
        url = pq(self.jsondata,"url")
        self.assertEqual(url, "http://www.tate.org.uk/art/artworks/"
                "hirst-controlled-substance-key-painting-ar00498")

    def test_multi_level(self):
        date_range = pq(self.jsondata, "dateRange.startYear")
        self.assertEqual(date_range, 1994)

    def test_array_index(self):
        birth_year = pq(self.jsondata, "contributors.0.birthYear")
        self.assertEqual(birth_year, 1965)

    def test_array(self):
        birth_year = pq(self.jsondata, "contributors.birthYear")
        self.assertEqual(birth_year, [1965])
        tags = pq(self.jsondata, "subjects.children.name")
        expectedtags = [u'abstraction', u'emotions, concepts and ideas',
                u'symbols & personifications', u'objects']
        self.assertEqual(set(tags), set(expectedtags))

    def test_array_index_out_of_bounds(self):
        invalid_data = pq(self.jsondata, "contributors.3.birthYear")
        self.assertEqual(invalid_data, None)

    def test_unexistent_index_in_json(self):
        url = pq(self.jsondata,"foo")
        self.assertEqual(url, None)

if __name__ == '__main__':
    unittest.main()
