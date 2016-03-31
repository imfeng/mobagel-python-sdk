__author__ = "alan4chen"

# ENV: python3.5.1 / python2.7.6

try:
    import pybagel
except:
    import sys
    import os
    filepath = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(filepath+'/..')
    import pybagel

# Initialize a Client Instance by product_key
c = pybagel.Client(product_key="1111111111222222222233333333334444444444555555555566666666667777")

# register a device_key by client
code, content = c.registerDevice()

# return a new device_key
print("Response code: ", code, " ,content:", content)