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

        my_device_config = {
        "product_id": "MoBagelSDK",
         "product_key": "1111111111222222222233333333334444444444555555555566666666667777",
         "device_id": "111111111122222222223333",
         "device_key": "1111111111222222222233333333334444444444555555555566666666667777"
        }

        self.myclient = pybagel.Client(device_config=my_device_config)




    #=========================================
    ### Test pybagel.Client() Time METHOD###

    @pytest.mark.usefixtures("init")
    def test_getTime_type(self):
        ret = self.myclient.getTime()
        assert type(ret) == str


    @pytest.mark.usefixtures("init")
    def test_getTime_time_in_range_of_an_hour(self):
        ret = self.myclient.getTime()
        assert abs(int(ret) - time.time()) < 36000000




    #=========================================
    ### Test pybagel.Client() sendReport METHOD###

    @pytest.mark.usefixtures("init")
    def test_sendReport_response201(self):
        report_content = {
                            "data": {
                                "state": "normal",
                                }
                         }
        ret = self.myclient.sendReport(report_content)
        assert json.loads(ret)['code'] == "201"
