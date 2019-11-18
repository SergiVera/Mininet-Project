#!/usr/bin/python

"In this python document we will define the topology of the network"

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info

class MyTopology(Topo):

    def __init__(self):

        "Initialize toplogy"
        Topo.__init__(self)

        "We create an empty network and we attachs the necessaris nodes and links to it"

        info("*** Adding hosts\n")
        h2p = self.addHost('h2p', ip = '169.0.10.3')
        h1a = self.addHost('h1a', ip = '169.0.10.4')
        h3p = self.addHost('h3p', ip = '169.0.10.5')
        h4p = self.addHost('h4p', ip = '169.0.10.6')

        info("*** Adding switches\n")
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')

        info("*** Creating links\n")
        self.addLink(s2,h2p)
        self.addLink(s2,h1a)
        self.addLink(s3,h3p)
        self.addLink(s3,h4p)
        self.addLink(s1,s2)
        self.addLink(s1,s3)

topos = { 'mytopo': (lambda: MyTopology())}



