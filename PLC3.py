import time 

from minicps.devices import PLC

from utils import PLC_PERIOD_SEC, PLC_SAMPLES
from utils import IP
from utils import STATE, PLC3_PROTOCOL, PLC3_DATA

from cpppo.server.enip.get_attribute import proxy_simple
from cpppo import logging

# Get IP Address
PLC1_ADDR = IP['plc1']
PLC2_ADDR = IP['plc2']
PLC3_ADDR = IP['plc3']

# Define sensors under plc1
P301 = ('P301', 3)



# Request value of FIT201 from PLC2
class PLC1Parameters(proxy_simple):
    PARAMETERS = dict(proxy_simple.PARAMETERS,
                      t101 = proxy_simple.parameter('@22/1/1', 'REAL', None),
    )

# Request value of LIT301 from PLC3
class PLC2Parameters(proxy_simple):
    PARAMETERS = dict(proxy_simple.PARAMETERS,
                      t201 = proxy_simple.parameter('@22/1/3', 'REAL', None),
    )

PLC1_COMMS = PLC1Parameters(host=PLC1_ADDR)
PLC2_COMMS = PLC2Parameters(host=PLC2_ADDR)



class PLC3(PLC):
    # Define pre_loop
    def pre_loop(self, sleep=1):
        print('DEBUG: plc3 enters pre_loop')
        time.sleep(sleep)
    
    # Define main_loop
    def main_loop(self):
        print('DEBUG: plc3 enters main_loop')     
        
        count = 0
        while(count <= PLC_SAMPLES):        
            # Get values from local sensors
            p301 = float(self.get(P301))
            print("DEBUG PLC3 - get p301: %f" % p301)

            # Get from PLC1
            params = PLC1_COMMS.parameter_substitution("t101")
            value, = PLC1_COMMS.read(params)
            time.sleep(0.1)
            # try:
            #     params = PLC1_COMMS.parameter_substitution("t101")
            #     value, = PLC1_COMMS.read(params)
            #     time.sleep(0.1) # wait to recive the value
            # except Exception as exc: 
            #     print ('t101 read error')
            #     # logging.warning("Access to fit201_2 at PLC2 failed: %s", exc)
            #     # PLC2_COMMS.close_gateway(exc)
            #     # raise

            t101 = float(value[0])
            print("\n\nPLC1: %f" % t101)


            # read from PLC3
            try:
                params = PLC2_COMMS.parameter_substitution("t201") # ("lit301_3")
                value, = PLC2_COMMS.read(params)
                time.sleep(0.1)
            except Exception as exc:
                logging.warning("Access to t201 at PLC2 failed: %s", exc)
                PLC2_COMMS.close_gateway(exc)
                raise

            t201 = float(value[0])
            print("\n\nPLC2: %f" % t201)


            time.sleep(PLC_PERIOD_SEC)
            count += 1
    

        print('DEBUG: plc3 shutdown')
            



if __name__ == "__main__":
    plc3 = PLC3(
        name='plc3',
        state=STATE,
        protocol=PLC3_PROTOCOL,
        memory=PLC3_DATA,
        disk=PLC3_DATA
    )