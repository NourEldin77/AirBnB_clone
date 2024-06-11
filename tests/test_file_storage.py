#!/usr/bin/python3

import unittest
import json
import os
from models.engine.file_storage import *
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.storage = FileStorage()
        self.test_obj = BaseModel()
        self.file_path = FileStorage._FileStorage__file_path
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_attributes(self):
        self.assertTrue(hasattr(self.storage, '_FileStorage__objects'), "storage should have '__objects'")
        self.assertTrue(hasattr(self.storage, '_FileStorage__file_path'), "storage should have '__file_path'")
        self.assertTrue(hasattr(self.storage, 'all'), "storage should have 'all()'")
        self.assertTrue(hasattr(self.storage, 'new'), "storage should have 'new()'")
        self.assertTrue(hasattr(self.storage, 'save'), "storage should have 'save()'")
        self.assertTrue(hasattr(self.storage, 'reload'),"storage should have 'reload()'")

    def test_all(self):
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        self.storage.new(self.test_obj)
        self.assertIn(f"BaseModel.{self.test_obj.id}", self.storage.all())

    def test_save(self):
        self.storage.new(self.test_obj)
        self.storage.save()
        with open(self.file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        self.assertIn(f"BaseModel.{self.test_obj.id}", data)

    def test_reload(self):
        self.storage.new(self.test_obj)
        self.storage.save()
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        self.assertIn(f"BaseModel.{self.test_obj.id}", self.storage.all())
