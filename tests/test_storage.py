import unittest
import json
import os
from models import storage
from models.base_model import BaseModel


class ExecutionTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        for attr in storage.__dict__:
            if "__objects" in attr:
                setattr(storage, attr, {})
        if (os.path.exists("storage.json")
                and os.path.isfile("storage.json")):
            os.remove("storage.json")

    def test_storage_application_instance(self):
        storage.save()
        with open("storage.json", "r") as f:
            compare_dict = json.loads(f.read())
        self.assertEqual({}, compare_dict)

    def test_storage_save_objects(self):
        instance_1 = BaseModel()
        instance_2 = BaseModel()
        self.assertTrue(all("BaseModel." in x for x in storage.all().keys()))

    def test_storage_look_for_file(self):
        storage.save()
        self.assertTrue(os.path.exists("storage.json")
                        and os.path.isfile("storage.json"))

    def test_storage_file_contains_objects(self):
        instance_1 = BaseModel()
        instance_2 = BaseModel()
        storage.save()
        with open("storage.json", "r") as f:
            compare_dict = json.loads(f.read())
        self.assertEqual(storage.all(), compare_dict)

    def test_storage_update_object(self):
        instance = BaseModel()
        instance.foo = 42
        instance.save()
        with open("storage.json", "r") as f:
            self.assertTrue("\"foo\": 42" in f.read())

    def cleanUp(self):
        for attr in storage.__dict__:
            if "__objects" in attr:
                setattr(storage, attr, {})
        os.remove("storage.json")
