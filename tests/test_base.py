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

    def test_create_instance_from_dict_of_a_previous_instance(self):
        instance = BaseModel()
        new_instance = BaseModel(**instance.to_dict())
        self.assertEqual(new_instance.id, instance.id)
        self.assertEqual(new_instance.created_at, instance.created_at)
        self.assertEqual(new_instance.updated_at, instance.updated_at)

    def test_create_instance_with_kwargs(self):
        instance = BaseModel(id=str(uuid.uuid4()),
                             created_at=datetime.now(),
                             updated_at=datetime.now())
        test_uuid = str(uuid.UUID(instance.id, version=4))
        self.assertEqual(test_uuid, instance.id)
        self.assertEqual(instance.created_at.date(), date.today())
        self.assertEqual(instance.updated_at.date(), date.today())

    def test_create_instance_with_additional_kwargs(self):
        instance = BaseModel(id=str(uuid.uuid4()),
                             created_at=datetime.now(),
                             updated_at=datetime.now(),
                             foo=42,
                             bar='baz')

        test_uuid = str(uuid.UUID(instance.id, version=4))
        self.assertEqual(test_uuid, instance.id)
        self.assertEqual(instance.created_at.date(), date.today())
        self.assertEqual(instance.updated_at.date(), date.today())
        self.assertEqual(instance.foo, 42)
        self.assertEqual(instance.bar, "baz")

    def test_create_instance_with_additional_kwargs_no_id_and_dates(self):
        instance = BaseModel(foo=42,
                             bar="baz")
        self.assertTrue(hasattr(instance, 'id'))
        self.assertTrue(hasattr(instance, 'created_at'))
        self.assertTrue(hasattr(instance, 'updated_at'))

        test_uuid = str(uuid.UUID(instance.id, version=4))
        self.assertEqual(test_uuid, instance.id)
        self.assertEqual(instance.created_at.date(), date.today())
        self.assertEqual(instance.updated_at.date(), date.today())
        self.assertEqual(instance.foo, 42)
        self.assertEqual(instance.bar, "baz")

    def test_create_instance_with_args(self):
        instance = BaseModel("Foo", 'bar', 96)
        self.assertTrue(hasattr(instance, 'id'))
        self.assertTrue(hasattr(instance, 'created_at'))
        self.assertTrue(hasattr(instance, 'updated_at'))

        test_uuid = str(uuid.UUID(instance.id, version=4))
        self.assertEqual(test_uuid, instance.id)
        self.assertEqual(instance.created_at.date(), date.today())
        self.assertEqual(instance.updated_at.date(), date.today())
