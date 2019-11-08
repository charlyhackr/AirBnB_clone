import unittest
import uuid
from datetime import datetime
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
        self.assertEqual(datetime(1973, 3, 1, 0, 23, 2), instance.created_at)

    def test_updated_at_is_a_datetime(self):
        instance = BaseModel()
        self.assertIsInstance(instance.updated_at, datetime)

    def test_updated_at_is_a_valid_datetime(self):
        instance = BaseModel()
        self.assertEqual(datetime(1973, 3, 1, 0, 23, 2), instance.updated_at)

    def test_base_model_str_representation(self):
        instance = BaseModel()
        self.assertTrue("[BaseModel] ({}) {{".format(instance.id) in str(instance))

    def  test_to_dic_type(self):
         tipo_dict = BaseModel()
         self.assertIsInstance(tipo_dict.to_dict(), dict)

    def test_to_dict_not_same(self):
        dic_not_same = BaseModel()
        self. assertNotEqual(dic_not_same.to_dict(), dic_not_same.__dict__)
