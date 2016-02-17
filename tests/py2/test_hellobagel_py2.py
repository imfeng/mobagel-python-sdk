
try:
    import pybagel
except:
    import sys
    import os
    filepath = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(filepath+'/../..')
    import pybagel


class Test_hellobagel:

    def test_hello(self):
        pybagel.hello()
        ## print "hello! pybagel!"
        ## for Testing
