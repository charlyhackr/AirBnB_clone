#!/usr/bin/python3
"""This file contains the tests for the FileStorage class."""
import unittest
import os
import json
import uuid
from datetime import datetime, date
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
        self.assertIsNotNone("takes no parameters" in str(context.exception))

    def test_check_type_of_file_storage_objects(self):
        instance = FileStorage()
        self.assertIsInstance(instance.all(), dict)

    def test_add_new_object_to_file_storage(self):
        instance = FileStorage()
        obj = BaseModel()
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
        BaseModel()
        BaseModel()
        instance.save()
        with open("storage.json", "r") as f:
            from_json = json.loads(f.read())
            all_instances = {key: value.to_dict()
                             for (key, value) in instance.all().items()}

        self.assertEqual(from_json, all_instances, "wrong dictionary")

    def test_reload_from_file(self):
        instance = FileStorage()
        BaseModel()
        BaseModel()
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

    def test_basemodel_instance(self):
        instance = BaseModel()
        self.assertIsInstance(instance, BaseModel)

    def test_id_is_a_uuid(self):
        instance = BaseModel()
        test_uuid = uuid.UUID(instance.id)
        self.assertIsInstance(test_uuid, uuid.UUID)

    def test_id_is_a_valid_v4_uuid(self):
        instance = BaseModel()
        test_uuid = uuid.UUID(instance.id, version=4)
        self.assertEqual(str(test_uuid), instance.id, "wrong UUID")

    def test_created_at_is_a_datetime(self):
        instance = BaseModel()
        self.assertIsInstance(instance.created_at, datetime)

    def test_created_at_is_a_valid_datetime(self):
        instance = BaseModel()
        self.assertTrue(date.today() == instance.created_at.date())

    def test_updated_at_is_a_datetime(self):
        instance = BaseModel()
        self.assertIsInstance(instance.updated_at, datetime)

    def test_updated_at_is_a_valid_datetime(self):
        instance = BaseModel()
        self.assertTrue(date.today() == instance.updated_at.date())

    def test_base_model_str_representation(self):
        instance = BaseModel()
        self.assertTrue("[BaseModel] ({}) {{".format(instance.id)
                        in str(instance))

    def test_base_model_save(self):
        instance = BaseModel()
        self.assertTrue(date.today() == instance.updated_at.date())
        prev_date = instance.updated_at
        instance.save()
        self.assertTrue(prev_date < instance.updated_at)

    def test_to_dic_type(self):
        tipo_dict = BaseModel()
        self.assertIsInstance(tipo_dict.to_dict(), dict)

    def test_to_dict_not_same(self):
        not_same = BaseModel()
        self.assertNotEqual(not_same.to_dict(), not_same.__dict__)

    def test_create_instance_from_dict_of_a_previous_instance(self):
        instance = BaseModel()
        new_instance = BaseModel(**instance.to_dict())
        self.assertEqual(new_instance.id, instance.id)
        self.assertEqual(new_instance.created_at, instance.created_at)
        self.assertEqual(new_instance.updated_at, instance.updated_at)

    def test_create_instance_with_kwarg_id_as_UUID_string(self):
        instance = BaseModel(id=str(uuid.uuid4()))
        test_uuid = str(uuid.UUID(instance.id, version=4))
        self.assertEqual(test_uuid, instance.id)

    def test_create_instance_with_kwarg_created_at_as_a_string(self):
        instance = BaseModel(created_at="1973-03-01T00:32:04.12345")
        self.assertEqual(instance.created_at,
                         datetime(1973, 3, 1, 0, 32, 4, 123450))

    def test_create_instance_with_kwarg_updated_at_as_a_string(self):
        instance = BaseModel(updated_at="2000-10-02T00:32:04.12345")
        self.assertEqual(instance.updated_at,
                         datetime(2000, 10, 2, 0, 32, 4, 123450))

    def test_create_instance_with_additional_kwarg(self):
        instance = BaseModel(id=str(uuid.uuid4()),
                             created_at=datetime.now(),
                             updated_at=datetime.now(),
                             foo=42)
        self.assertEqual(hasattr(instance, "foo") and instance.foo, 42)

    def test_create_instance_additional_kwargs_no_id_and_dates(self):
        instance = BaseModel(bar="baz")
        self.assertTrue(hasattr(instance, 'id')
                        and hasattr(instance, 'created_at')
                        and hasattr(instance, 'updated_at'))

        self.assertEqual(hasattr(instance, "bar") and instance.bar, "baz")

    def test_create_basemodel_instance_with_args(self):
        instance = BaseModel("Foo", 'bar', 96)
        self.assertTrue(hasattr(instance, 'id')
                        and hasattr(instance, 'created_at')
                        and hasattr(instance, 'updated_at'))

    def test_instance_args_no_extra_attributes_are_created(self):
        instance = BaseModel("Foo", 'bar', 96)
        self.assertTrue(("foo", 'bar', 96) not in instance.__dict__.values())
