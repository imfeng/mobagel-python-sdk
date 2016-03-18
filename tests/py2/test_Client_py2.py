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
    ### Test pybagel.Client() Time METHOD###

    @pytest.mark.usefixtures("init")
    def test_getTime_type(self):
        ret = self.myclient.getTime()
        assert type(ret) == str or type(ret) == unicode


    @pytest.mark.usefixtures("init")
    def test_getTime_time_in_range_of_an_hour(self):
        ret = self.myclient.getTime()
        assert abs(int(ret) - time.time()) < 36000000


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
        assert "data" in ret
        assert "timestamp" in ret


    #=========================================
    ### Test pybagel.Client() registerDevice METHOD###
    @pytest.mark.usefixtures("init")
    def test_registerDevice(self):
        new_device_key = self.myclient.registerDevice()
        assert (type(new_device_key) == unicode or type(new_device_key) == str)

