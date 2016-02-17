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
            "product_id": "TestAlanProduct",
            "product_key": "e1364fcb287215e8804b7185193ffb294188321f50be996df16904bccfcbd92f",
            "device_id": "56c43ae3f8e9d3a12f8b4567",
            "device_key": "0be77e401484c3f6929783f023a2afd2ae45e5b917214c21142ee6e8ee15551b"}

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
        assert abs(int(ret) - time.time()*1000) < 36000000




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
        assert json.loads(ret)['code'] == 201
