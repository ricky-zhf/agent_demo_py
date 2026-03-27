# -*- coding: utf-8 -*-

import unittest

from src.quick_start.hugging_face import hugging_face_demo


class TestHugging(unittest.TestCase):
    def test_hugging(self):
        hugging_face_demo()
