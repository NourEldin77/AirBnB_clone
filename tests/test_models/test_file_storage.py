#!/usr/bin/python3

import unittest
from models.engine.file_storage import *


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.obj = FileStorage()

    def test_attributes(self):
        self.assertTrue(hasattr(self.obj, '_FileStorage__objects'), "obj should have '__objects'")
        self.asserTrue(hasattr(self.obj, '_FileStorage__file_path'), "obj should have '__file_path'")
        self.assertTrue(hasattr(self.obj, 'all'), "obj should have 'all()'")
        self.assertTrue(hasattr(self.obj, 'new'), "obj should have 'new()'")
        self.assertTrue(hasattr(self.obj, 'save'), "obj should have 'save()'")
        self.assertTrue(hasattr(self.obj, 'reload'),"obj should have 'reload()'")


