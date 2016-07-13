"""
This example creates a GRE Tunnel between OpenVSwitch s1 and OpenVSwitch s2.

h1---s1--[GRE-TUNNEL]--s2---h1

"""

from mininet.net import Mininet
from mininet.node import Controller, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel

def greTunnelNet():

    net = Mininet( controller=Controller, switch=OVSSwitch )

    print( "*** Creating (reference) controllers" )
    c1 = net.addController( 'c1', port=6633 )
    c2 = net.addController( 'c2', port=6634 )

    print( "*** Creating switches" )
    s1 = net.addSwitch( 's1' )
    s2 = net.addSwitch( 's2' )

    print( "*** Creating hosts" )
    hosts1 = [ net.addHost( 'h%d' % n ) for n in ( 3, 4 ) ]
    hosts2 = [ net.addHost( 'h%d' % n ) for n in ( 5, 6 ) ]

    print( "*** Creating links" )
    for h in hosts1:
        net.addLink( s1, h )
    for h in hosts2:
        net.addLink( s2, h )
        net.addLink( s1, s2 )

    print( "*** Creating GRE Tunnel" )

    print( "*** Starting network" )
    net.build()
    c1.start()
    c2.start()
    s1.start( [ c1 ] )
    s2.start( [ c2 ] )

    print( "*** Testing network" )
    net.pingAll()

    print( "*** Running CLI" )
    CLI( net )

    print( "*** Stopping network" )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )  # for CLI output
    greTunnelNet()
