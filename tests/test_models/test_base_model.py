#!/usr/bin/python3
"""

Defines unittests for models/base_model.py.

"""

import unittest
import models
import os
from uuid import uuid4
from  datetime import datetime
from models.base_model import BaseModel
from time import sleep


class Test_BaseModel(unittest.TestCase):
    """testing case for BasesModel class."""

    def setUp(self):
        """sets up environment for each test case."""
        self.model = BaseModel()

    def tearDown(self):
        """cleans the environment after each test if needed"""
        pass

    def test_init_with_arguments(self):
        """test initialization with argumentas(kwargs)"""

        args ={
                'id': '123',
                'created_at': '2023-12-01T00:00:00',
                "updated_at": '2023-12-01T00:00:00',
                "name": "Test",
        }

        base_model = BaseModel(**args)

        #check attributes are set correctly

        self.assertEqual(base_model.id, '123')
        self.assertEqual(base_model.created_at,
                datetime.fromisoformat('2023-12-01T00:00:00'))
        self.assertEqual(base_model.updated_at,
                datetime.fromisoformat('2023-12-01T00:00:00'))
        self.assertEqual(base_model.name, 'Test')


    def test_init_without_arguments(self):
        """test without arguments"""
        base_model = BaseModel()

        #check attributes are set correctly
        self.assertIsNotNone(base_model.id)
        self.assertIsNotNone(base_model.created_at)
        self.assertIsNotNone(base_model.updated_at)
        self.assertEqual(base_model.created_at, base_model.updated_at)


if __name__ == "__main__":
    unittest.main()
