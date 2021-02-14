# -*- coding:utf-8 -*-
"""
  @file get_ozone_data.py
  @brief get ozone concentration, A concentration of one part per billion (PPB).
  @n step: we must first determine the iic device address, will dial the code switch A0, A1 (ADDRESS_0 for [0 0]), (ADDRESS_1 for [1 0]), (ADDRESS_2 for [0 1]), (ADDRESS_3 for [1 1]).
  @n       Then configure the mode of active and passive acquisition, Finally, ozone data can be read.
  @n note: it takes time to stable oxygen concentration, about 3 minutes.
  @copyright   Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
  @licence     The MIT License (MIT)
  @author      [ZhixinLiu](zhixin.liu@dfrobot.com)
  version  V1.0
  date  2020-5-27
  @get from https://www.dfrobot.com
  @url https://github.com/DFRobot/DFRobot_Oxygen
"""
import sys
import time
import math

from lib.dfrobot_oxygen import DFRobot_Oxygen_IIC, ADDRESS_3

COLLECT_NUMBER = 10  # collect number, the collection range is 1-100
IIC_MODE = 0x01  # default use IIC1
"""
   # The first  parameter is to select iic0 or iic1
   # The second parameter is the iic device address
   # The default address for iic is ADDRESS_3
   # ADDRESS_0                 = 0x70
   # ADDRESS_1                 = 0x71
   # ADDRESS_2                 = 0x72
   # ADDRESS_3                 = 0x73
"""
oxygen = DFRobot_Oxygen_IIC(IIC_MODE, ADDRESS_3)
while 1:
    """ Smooth data collection £¬the collection range is 1-100 """
    oxygen_data = oxygen.get_oxygen_data(COLLECT_NUMBER)
    print("Oxygen concentration is %4.2f %%vol" % oxygen_data)
    time.sleep(1)
