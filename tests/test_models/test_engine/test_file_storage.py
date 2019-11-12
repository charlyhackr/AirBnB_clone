"""
This file contains the tests for the FileStorage class
"""
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

    def test_create_instance_with_args(self):
        with (self.assertRaises(TypeError)) as context:
            instance = FileStorage(1)
        self.assertTrue("takes no parameters" in str(context.exception))

    def test_check_type_of_file_storage_objects(self):
        instance = FileStorage()
        self.assertIsInstance(instance.all(), dict)

    def test_add_new_object_to_file_storage(self):
        instance = FileStorage()
        obj = BaseModel()
        instance.new(obj)
        self.assertIn(obj,
                      instance.all().values(),
                      "object isn't in file storage")

    def test_generate_file(self):
        instance = FileStorage()
        instance.save()
        self.assertTrue(os.path.exists("storage.json") and
                        os.path.isfile("storage.json"))

    def test_save_with_args(self):
        instance = FileStorage()
        with (self.assertRaises(TypeError)) as context:
            instance.save(98)
        self.assertTrue("save() takes 1 positional argument" in
                        str(context.exception))

    def test_add_new_object_and_save_to_file(self):
        instance = FileStorage()
        instance.new(BaseModel())
        instance.new(BaseModel())
        instance.save()
        with open("storage.json", "r") as f:
            from_json = json.loads(f.read())
            all_instances = {key: value.to_dict()
                             for (key, value) in instance.all().items()}

        self.assertEqual(from_json, all_instances, "wrong dictionary")

    def test_reload_from_file(self):
        instance = FileStorage()
        instance.new(BaseModel())
        instance.new(BaseModel())
        instance.save()
        del instance
        new_instance = FileStorage()
        new_instance.reload()
        with open("storage.json", "r") as f:
            from_json = json.loads(f.read())
            all_instances = {key: value.to_dict()
                             for (key, value) in new_instance.all().items()}

        self.assertEqual(from_json, all_instances, "wrong dictionary")

    def test_reload_from_nonexistent_file(self):
        instance = FileStorage()
        instance.reload()
        instance.save()
        self.assertEqual({}, instance.all())

    def test_reload_with_args(self):
        instance = FileStorage()
        with (self.assertRaises(TypeError)) as context:
            instance.reload(98)
        self.assertTrue("reload() takes 1 positional argument" in
                        str(context.exception))

    def tearDown(self):
        for attr in FileStorage.__dict__:
            if "__objects" in attr:
                setattr(FileStorage, attr, {})
        if (os.path.exists("storage.json")
                and os.path.isfile("storage.json")):
            os.remove("storage.json")
