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

my_device_config = {
        "product_id": "MoBagelSDK",
         "product_key": "1111111111222222222233333333334444444444555555555566666666667777",
         "device_id": "111111111122222222223333",
         "device_key": "1111111111222222222233333333334444444444555555555566666666667777"
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

