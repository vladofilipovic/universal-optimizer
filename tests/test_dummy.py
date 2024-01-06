
import unittest   
import unittest.mock as mocker

class TestDummy(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("setUpClass TestDummy\n")

    def setUp(self):
        self.dummy_val = 42

        self.dummy_stub = mocker.MagicMock()
        type(self.dummy_stub).function = mocker.Mock(return_value = lambda x:42)

        self.dummy_mock = mocker.MagicMock()
        type(self.dummy_mock).name = mocker.PropertyMock(return_value='some_problem')
        type(self.dummy_mock).dimension = mocker.PropertyMock(return_value=42)

    
    def test_dummy_obj_name_should_be_some_problem(self):
        self.assertEqual(self.dummy_mock.name, 'some_problem')

    def test_dummy_obj_dimension_should_be_42(self):
        self.assertEqual(self.dummy_mock.dimension, 42)

    def test_dummy_obj_dimension_should_be_dummy_val(self):
        self.assertEqual(self.dummy_mock.dimension, self.dummy_val)

    def tearDown(self):
        return

    @classmethod
    def tearDownClass(cls):
        print("\ntearDownClass TestDummy")
    
if __name__ == '__main__':
    unittest.main()