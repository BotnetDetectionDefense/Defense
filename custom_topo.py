from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel

class DoubleSwitchTopo( Topo ):
    "Two switches connected to 2 hosts each."
    def build( self, n=4 ):
	s1 = self.addSwitch( 's1' )
        s2 = self.addSwitch( 's2' ) 
	h1 = self.addHost( 'h1' )
	h2 = self.addHost( 'h2' )
        h3 = self.addHost( 'h3' )
        h4 = self.addHost( 'h4' )
	    # 10 Mbps, 5ms delay, 2% loss, 1000 packet queue
	self.addLink( h1, s1)
        self.addLink( h2, s1 )
        self.addLink( h3, s2 )
        self.addLink( h4, s2 )
	self.addLink( s1, s2 )


# Allows the file to be imported using `mn --custom <filename> --topo minimal`
topos = {
    'double': DoubleSwitchTopo
}
