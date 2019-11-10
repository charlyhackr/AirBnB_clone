import unittest
import json
import os
from models import storage
from models.base_model import BaseModel


class ExecutionTestCase(unittest.TestCase):

    def test_storage_application_instance(self):
        storage.save()
        with open("storage.json", "r") as f:
            compare_dict = json.loads(f.read())
        self.assertEqual({}, compare_dict)

    def test_storage_save_objects(self):
        storage.new(BaseModel())
        storage.new(BaseModel())
        self.assertTrue(all("BaseModel." in x for x in storage.all().keys()))

    def test_storage_look_for_file(self):
        storage.save()
        self.assertTrue(os.path.exists("storage.json")
                        and os.path.isfile("storage.json"))

    def test_storage_file_contains_objects(self):
        storage.new(BaseModel())
        storage.new(BaseModel())
        storage.save()
        with open("storage.json", "r") as f:
            compare_dict = json.loads(f.read())
        self.assertEqual(storage.all(), compare_dict)

    def cleanUp(self):
        for attr in storage.__dict__:
            if "__objects" in attr:
                setattr(storage, attr, {})
        os.remove("storage.json")
