from mininet.topo import Topo

class MyTopo( Topo ):
   # "Simple topology example."

    def __init__( self ):
     #   "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        leftHost = self.addHost( 'h1' )
        rightHost = self.addHost( 'h2' )
        thirdHost = self.addHost( 'h3' )
        fourthHost = self.addHost( 'h4' )
        leftSwitch = self.addSwitch( 's1' )
        rightSwitch = self.addSwitch( 's2' )
        thirdswitch = self.addSwitch( 's3' )
        fourthswitch = self.addSwitch( 's4' )
        # Add links
        self.addLink( leftHost, leftSwitch )
        self.addLink( leftSwitch, rightSwitch )
        self.addLink( rightSwitch, rightHost )
        self.addLink( rightSwitch, thirdSwitch )
        self.addLink( thirdSwitch, thirdHost )
        self.addLink( rightSwitch, fourthSwitch )
        self.addLink( fourthSwitch, fourthHost )


topos = { 'mytopo': ( lambda: MyTopo() ) }