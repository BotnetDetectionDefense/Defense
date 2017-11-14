from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel

class FourSwitchTopo( Topo ):
    "Four switches connected to 4 hosts each."
    def build( self, n=4 ):
        s1 = self.addSwitch( 's1' )
    	s2 = self.addSwitch( 's2' )
        s3 = self.addSwitch( 's3' )
    	s4 = self.addSwitch( 's4' )
    	h1 = self.addHost( 'h1' )
    	h2 = self.addHost( 'h2' )
        h3 = self.addHost( 'h3' )
        h4 = self.addHost( 'h4' )
        h5 = self.addHost( 'h5' )
        h6 = self.addHost( 'h6' )
        h7 = self.addHost( 'h7' )
        h8 = self.addHost( 'h8' )
        h9 = self.addHost( 'h9' )
        h10 = self.addHost( 'h10' )
        h11 = self.addHost( 'h11' )
        h12 = self.addHost( 'h12' )
        server1 = self.addHost( 'server1' )
        server2 = self.addHost( 'server2' )
        server3 = self.addHost( 'server3' )
    
        self.addLink( server1, s1)
        self.addLink( server2, s1 )
        self.addLink( server3, s1 )
        self.addLink( h1, s2 )
        self.addLink( h2, s2 )
        self.addLink( h3, s2 )
        self.addLink( h4, s2 )
        self.addLink( h5, s3 )
        self.addLink( h6, s3 )
        self.addLink( h7, s3 )
        self.addLink( h8, s3 )
        self.addLink( h9, s4 )
        self.addLink( h10, s4 )
        self.addLink( h11, s4 )
        self.addLink( h12, s4 )
        self.addLink( s1, s2 )
        self.addLink( s2, s3 )
        self.addLink( s3, s4 )

	

# Allows the file to be imported using `mn --custom <filename> --topo demo
topos = {
    'demo': FourSwitchTopo
}