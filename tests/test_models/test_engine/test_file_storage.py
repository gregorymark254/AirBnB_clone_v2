import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        """Set up a clean environment before each test."""
        self.file_path = 'file.json'
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = self.file_path

    def tearDown(self):
        """Clean up after each test."""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all_method_returns_dictionary(self):
        """Test if the all method returns a dictionary."""
        result = self.storage.all()
        self.assertIsInstance(result, dict)

    def test_new_method_adds_object(self):
        """Test if the new method adds an object to the storage dictionary."""
        obj = BaseModel()
        key = "{}.{}".format(obj.__class__.__name__, obj.id)

        self.storage.new(obj)
        result = self.storage.all()

        self.assertIn(key, result)

    def test_save_method_saves_to_file(self):
        """Test if the save method saves the storage dictionary to a file."""
        obj = BaseModel()
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.storage.new(obj)
        self.storage.save()

        with open(self.file_path, 'r') as f:
            data = f.read()
            self.assertIn(key, data)

    def test_reload_method_loads_from_file(self):
        """Test if the reload method loads the storage dictionary from a file."""
        obj = BaseModel()
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.storage.new(obj)
        self.storage.save()

        new_storage = FileStorage()
        new_storage._FileStorage__file_path = self.file_path
        new_storage.reload()

        result = new_storage.all()

        self.assertIn(key, result)

    def test_delete_method_removes_object(self):
        """Test if the delete method removes an object from the storage dictionary."""
        obj = BaseModel()
        key = "{}.{}".format(obj.__class__.__name__, obj.id)

        self.storage.new(obj)
        self.storage.delete(obj)
        result = self.storage.all()

        self.assertNotIn(key, result)

    def test_all_method_returns_filtered_list(self):
        """Test if the all method returns a filtered list based on the provided class."""
        obj1 = BaseModel()
        obj2 = BaseModel()
        obj3 = BaseModel()

        self.storage.new(obj1)
        self.storage.new(obj2)
        self.storage.new(obj3)


if __name__ == '__main__':
    unittest.main()
