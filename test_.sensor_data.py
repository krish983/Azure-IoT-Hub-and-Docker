#Dependencies

import unittest  #Unit-test module
from server import *  #Application Source code directory

#Class declaration for testing

class TestData(unittest.TestCase):

    #Method for test caluculation
    
    def test_volume(self):

        self.assertAlmostEqual(sensor_values(2),1)  #Wrong Test case
        self.assertAlmostEqual(sensor_values(1),1)  # 1*1*1 = 1 Correct test cse
        self.assertAlmostEqual(sensor_values(3),27)  #Correct test case
        self.assertAlmostEqual(sensor_values(5.5),166.375)  #Correct test case