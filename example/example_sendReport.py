__author__ = "alan4chen"

# ENV: python3.5.1 / python2.7.6
import json

try:
    import pybagel

except:
    import sys
    import os
    filepath = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(filepath+'/..')
    import pybagel

# Initialize a Client Instance by product_key
# c = pybagel.Client(product_key="<$PRODUCT-KEY>")
c = pybagel.Client(product_key="1111111111222222222233333333334444444444555555555566666666667777")

# You can register a device and get a device_key according "example_registerDevice.py"
# format: device_key = <Your Device Key>
device_key = "1111111111222222222233333333334444444444555555555566666666667777"

# set Content:
content={
            "state": "Put your state here!",
            "c_customization" : "python_sdk_test",
            "c_develop_zone" : "PythonSDK"
}

# SendReport
code, ret = c.sendReport(
    device_key = device_key,
    content = content,
)

# return report_status (success:201) and report_data
print(code, ret)
