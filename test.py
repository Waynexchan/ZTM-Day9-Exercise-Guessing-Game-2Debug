import unittest
import main

class TestMain(unittest.TestCase):
  def setUp(self):
    print('Start to test the function')
  def test_input(self):
    test_input = 5
    test_answer = 5
    result = main.guess_input(test_input,test_answer)
    self.assertTrue(result)

  def test_String(self):
    test_input = 'me'
    test_answer = 5
    result = main.guess_input(test_input,test_answer)
    self.assertIsInstance(result,ValueError)

  def test_None(self):
    test_input = None
    test_answer = 5
    result = main.guess_input(test_input,test_answer)
    self.assertFalse(result)

  def test_Empty(self):
    test_input = ''
    test_answer = 5
    result = main.guess_input(test_input,test_answer)
    self.assertFalse(result)

  def test_wrong_input(self):
    test_input = 0
    test_answer = 5
    result = main.guess_input(test_input,test_answer)
    self.assertFalse(result)

  def tearDown(self):
    print('Test finished')

if __name__ == '__main__':
    unittest.main()