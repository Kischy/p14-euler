# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 19:50:22 2019

@author: kisch
"""


import unittest

from collatz_sequence_length import len_of_collatz_sequence as l_cs


class TestCollatzLength(unittest.TestCase):
    
    def test_len_of_collatz_sequence_testcase(self):
        self.assertEqual(l_cs(13),10)



if __name__ == '__main__':
    unittest.main(verbosity=0)
