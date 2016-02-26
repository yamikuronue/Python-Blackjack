from helloWorld import greet
import unittest

class TestGreet(unittest.TestCase):

  def test_greet(self):
      self.assertEqual(greet("Hello"), "Hello Hello");
	  
if __name__ == '__main__':
    unittest.main()