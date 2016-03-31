try:
    import pybagel
except:
    import sys
    import os
    filepath = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(filepath+'/../..')
    import pybagel

import pytest
import time
import json


class Test_Client:

    @pytest.fixture()
    def init(self):
        self.myclient = pybagel.Client(product_key="1111111111222222222233333333334444444444555555555566666666667777")

    #=========================================
    ### Test pybagel.Client() sendReport METHOD###

    @pytest.mark.usefixtures("init")
    def test_sendReport_response201(self):
        report_content = {
                            "state": "normal",
                            "c_customization": "py2test"
                         }
        ret = self.myclient.sendReport(device_key="1111111111222222222233333333334444444444555555555566666666667777",
                                       content=report_content)


    #=========================================
    ### Test pybagel.Client() registerDevice METHOD###
    @pytest.mark.usefixtures("init")
    def test_registerDevice(self):
        self.myclient.registerDevice()

