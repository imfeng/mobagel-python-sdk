__author__ = "alan4chen"

# ENV: python3.5.1

try:
    import pybagel
except:
    import sys
    import os
    filepath = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(filepath+'/..')
    import pybagel

import pytest
import time
import json


my_device_config = {
    "product_id": "TestAlanProduct",
    "product_key": "e1364fcb287215e8804b7185193ffb294188321f50be996df16904bccfcbd92f",
    "device_id": "56c43ae3f8e9d3a12f8b4567",
    "device_key": "0be77e401484c3f6929783f023a2afd2ae45e5b917214c21142ee6e8ee15551b"
    }

myclient = pybagel.Client(device_config=my_device_config)

print(myclient.getTime().decode())

report_content = {
                    "data": {
                        "state": "normal",   ## state field is necessary
                        }
                 }

ret = myclient.sendReport(report_content)

print(ret)

