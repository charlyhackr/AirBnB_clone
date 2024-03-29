#!/usr/bin/python3
"""
This file contains the test for the `storage` `FileStorage` global instance
"""
import unittest
import json
import os
from models import storage
from models.base_model import BaseModel


class StorageTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        for attr in storage.__class__.__dict__:
            if "__objects" in attr:
                setattr(storage.__class__, attr, {})
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
        self.assertTrue(all("BaseModel." in x for x in storage.all()))

    def test_storage_look_for_file(self):
        storage.save()
        self.assertTrue(os.path.exists("storage.json")
                        and os.path.isfile("storage.json"))

    def test_storage_file_contains_objects(self):
        instance_1 = BaseModel()
        instance_2 = BaseModel()
        storage.save()
        with open("storage.json", "r") as f:
            from_json = json.loads(f.read())
            all_instances = {key: value.to_dict()
                             for (key, value) in storage.all().items()}

        self.assertEqual(all_instances, from_json)

    def test_storage_update_object(self):
        instance = BaseModel()
        instance.foo = 42
        instance.save()
        with open("storage.json", "r") as f:
            self.assertTrue("\"foo\": 42" in f.read())

    def tearDown(self):
        for attr in storage.__class__.__dict__:
            if "__objects" in attr:
                setattr(storage.__class__, attr, {})
        if (os.path.exists("storage.json")
                and os.path.isfile("storage.json")):
            os.remove("storage.json")
