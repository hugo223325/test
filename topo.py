# -*- coding: utf-8 -*-

from mininet.topo import Topo
from utils import IP, MAC, NETMASK

class CigaretteFactoryTopo(Topo):
    def build(self):
        switch = self.addSwitch('s1')

        plc1 = self.addHost(
            'plc1',
            ip=IP['plc1'] + NETMASK,
            mac=MAC['plc1'])
        self.addLink(plc1, switch)

        plc2 = self.addHost(
            'plc2',
            ip=IP['plc2'] + NETMASK,
            mac=MAC['plc2'])
        self.addLink(plc2, switch)

        plc3 = self.addHost(
            'plc3',
            ip=IP['plc3'] + NETMASK,
            mac=MAC['plc3'])
        self.addLink(plc3, switch)

        scada = self.addHost(
            'scada',
            ip=IP['scada'] + NETMASK,
            mac=MAC['scada'])
        self.addLink(scada, switch)

        attacker = self.addHost(
            'attacker',
            ip=IP['attacker'] + NETMASK,
            mac=MAC['attacker'])
        self.addLink(attacker, switch)




