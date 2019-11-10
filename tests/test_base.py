import unittest
import uuid
from datetime import datetime, date
from models.base_model import BaseModel


class BaseModelTestCase(unittest.TestCase):

    def test_instance(self):
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
