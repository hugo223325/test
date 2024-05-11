from mininet.net import Mininet
from mininet.cli import CLI
from minicps.mcps import MiniCPS

from topo import CigaretteFactoryTopo

import sys

class CigaretteFactorySimulator(MiniCPS):
    """Main container used to run the simulation."""

    def __init__(self, name, net):
        self.name = name
        self.net = net
        net.start()

        net.pingAll()

        # start devices
        plc1, plc2, plc3, s1, scada = self.net.get(
            'plc1', 'plc2', 'plc3', 's1', 'scada')
        # plc1, plc2, plc3, s1 = self.net.get(
        #     'plc1', 'plc2', 'plc3', 's1')

        # SPHINX_SWAT_TUTORIAL RUN(
        scada.cmd(sys.executable + ' -u ' + ' init.py  &> logs/init.log &')
        plc1.cmd(sys.executable + ' -u ' + ' PLC1.py  &> logs/plc1.log &')
        plc3.cmd(sys.executable + ' -u ' + ' PLC3.py  &> logs/plc3.log &')
        plc2.cmd(sys.executable + ' -u ' + ' PLC2.py  &> logs/plc2.log &')


        s1.cmd(sys.executable + ' -u ' + ' physical_process.py  &> logs/process.log &')
        # SPHINX_SWAT_TUTORIAL RUN)
        CLI(self.net)

        net.stop()



if __name__ == "__main__":
    topo = CigaretteFactoryTopo()
    net = Mininet(topo=topo)

    cigarette_cps = CigaretteFactorySimulator(
        name='cigarette',
        net=net)
