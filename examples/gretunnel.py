"""
This example creates a GRE Tunnel between OpenVSwitch s1 and OpenVSwitch s2.

h1---s1--[GRE-TUNNEL]--s2---h1

"""

from mininet.net import Mininet
from mininet.node import Controller, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel

def greTunnelNet():
    pass

if __name__ == '__main__':
    setLogLevel( 'info' )  # for CLI output
    greTunnelNet()
