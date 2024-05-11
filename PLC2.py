import time 

from minicps.devices import PLC


from utils import PLC_PERIOD_SEC, PLC_SAMPLES
from utils import IP
from utils import STATE, PLC2_PROTOCOL, PLC2_DATA


import shlex
import subprocess
from cpppo.server.enip.get_attribute import proxy_simple


# Get IP Address
PLC1_ADDR = IP['plc1']
PLC2_ADDR = IP['plc2']
PLC3_ADDR = IP['plc3']

# Define sensors under plc1
T201 = ('T201', 2)
H201 = ('H201', 2)
F201 = ('F201', 2)


class PLC2(PLC):
    # Define pre_loop
    def pre_loop(self, sleep=0.1):
        print('DEBUG: plc2 enters pre_loop')
        time.sleep(sleep)
    
    # Define main_loop
    def main_loop(self):
        print('DEBUG: plc2 enters main_loop')


        # Start enip server with dummy values (to be updated for each "PLC_SAMPLE" loop)
        tag_string = 'T201:3@22/1/3=REAL'
        cmd = shlex.split(
            'enip_server --print' +
            ' ' + tag_string
        )
        
        # Start server in the background
        try:
            client = subprocess.Popen(cmd, shell=False)
            time.sleep(1) # wait for server to start

        except Exception as error:
            print('ERROR plc2 error starting server: ', error)
            exit(1)

        via = proxy_simple('192.168.1.20')
        t201_tag = '@22/1/3'
        
        
        count = 0
        while(count <= PLC_SAMPLES):        
            # Get values from local sensors
            t201 = float(self.get(T201))
            print("DEBUG PLC2 - get t201: %f" % t201)
            
            h201 = float(self.get(H201))
            print("DEBUG PLC2 - get h201: %f" % h201)
            
            f201 = float(self.get(F201))
            print("DEBUG PLC2 - get h201: %f" % f201)


            # Send relevent sensor values to PLC3
            # self.send(T101, t101, PLC3_ADDR)
            with via: result, = via.read([(t201_tag + '=(REAL)' + str(t201), t201_tag)])
            print('this is the return value: %s' % result)


            time.sleep(PLC_PERIOD_SEC)
            count += 1
    

        print('DEBUG: plc1 shutdown')
            



if __name__ == "__main__":
    plc2 = PLC2(
        name='plc2',
        state=STATE,
        protocol=PLC2_PROTOCOL,
        memory=PLC2_DATA,
        disk=PLC2_DATA
    )