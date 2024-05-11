import time 

from minicps.devices import PLC


from utils import PLC_PERIOD_SEC, PLC_SAMPLES
from utils import IP
from utils import STATE, PLC1_PROTOCOL, PLC1_DATA


import shlex
import subprocess
from cpppo.server.enip.get_attribute import proxy_simple


# Get IP Address
PLC1_ADDR = IP['plc1']
PLC2_ADDR = IP['plc2']
PLC3_ADDR = IP['plc3']

# Define sensors under plc1
T101 = ('T101', 1)
H101 = ('H101', 1)


class PLC1(PLC):
    # Define pre_loop
    def pre_loop(self, sleep=0.1):
        print('DEBUG: plc1 enters pre_loop')
        time.sleep(sleep)
    
    # Define main_loop
    def main_loop(self):
        print('DEBUG: plc1 enters main_loop')


        # Start enip server with dummy values (to be updated for each "PLC_SAMPLE" loop)
        tag_string = 'T101:2@22/1/1=REAL'
        cmd = shlex.split(
            'enip_server --print' +
            ' ' + tag_string
        )
        
        # Start server in the background
        try:
            client = subprocess.Popen(cmd, shell=False)
            time.sleep(1) # wait for server to start

        except Exception as error:
            print('ERROR plc1 error starting server: ', error)
            exit(1)

        via = proxy_simple('192.168.1.10')
        t101_tag = '@22/1/1'
        
        
        count = 0
        while(count <= PLC_SAMPLES):        
            # Get values from local sensors
            t101 = float(self.get(T101))
            print("DEBUG PLC1 - get t101: %f" % t101)
            
            h101 = float(self.get(H101))
            print("DEBUG PLC1 - get h101: %f" % h101)


            # Send relevent sensor values to PLC3
            # self.send(T101, t101, PLC3_ADDR)
            with via: result, = via.read([(t101_tag + '=(REAL)' + str(t101), t101_tag)])
            print('this is the return value: %s' % result)


            time.sleep(PLC_PERIOD_SEC)
            count += 1
    

        print('DEBUG: plc1 shutdown')
            



if __name__ == "__main__":
    plc1 = PLC1(
        name='plc1',
        state=STATE,
        protocol=PLC1_PROTOCOL,
        memory=PLC1_DATA,
        disk=PLC1_DATA
    )