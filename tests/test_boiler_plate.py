#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_boiler_plate
----------------------------------

Tests for `boiler_plate` module.
"""

import unittest

import boiler_plate


class TestBoiler_plate(unittest.TestCase):

    def setUp(self):
        self.hello_message = "Hello, World!"

    def test_prints_hello_world(self):
        output = boiler_plate.hello()
        assert output == self.hello_message

    def test_something(self):
        assert(boiler_plate.__version__)

    def tearDown(self):
        pass
