import unittest
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class FileStorageTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        os.remove("storage.json")

    def test_create_instance(self):
        instance = FileStorage()
        self.assertIsInstance(instance, FileStorage)

    def test_check_type_of_file_storage_objects(self):
        instance = FileStorage()
        self.assertIsInstance(instance.all(), dict)

    def test_add_new_object_to_file_storage(self):
        instance = FileStorage()
        obj = BaseModel()
        instance.new(obj)
        self.assertIn(obj.to_dict(),
                      instance.all().values(),
                      "object isn't in file storage")

    def test_generate_file(self):
        instance = FileStorage()
        instance.save()
        self.assertTrue(os.path.exists("storage.json") and
                        os.path.isfile("storage.json"))

    def test_add_new_object_and_save_to_file(self):
        instance = FileStorage()
        instance.new(BaseModel())
        instance.new(BaseModel())
        instance.save()
        with open("storage.json", "r") as f:
            compare_dict = json.loads(f.read())
        self.assertEqual(compare_dict, instance.all(), "wrong dictionary")

    def test_reload_from_file(self):
        instance = FileStorage()
        instance.new(BaseModel())
        instance.new(BaseModel())
        instance.save()
        del instance
        new_instance = FileStorage()
        new_instance.reload()
        with open("storage.json", "r") as f:
            compare_dict = json.loads(f.read())
        self.assertEqual(compare_dict, new_instance.all(), "wrong dictionary")

    def test_reload_from_nonexistent_file(self):
        instance = FileStorage()
        instance.reload()
        instance.save()
        self.assertEqual({}, instance.all())

    def tearDown(self):
        for attr in FileStorage.__dict__:
            if "__objects" in attr:
                setattr(FileStorage, attr, {})
        if (os.path.exists("storage.json")
                and os.path.isfile("storage.json")):
            os.remove("storage.json")
