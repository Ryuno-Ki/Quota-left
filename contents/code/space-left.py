#!/usr/bin/env python
# -*- coding: utf-8 -*-

########################################################################
# space-left                                                           #
# shows the space left for mathematic students at University Stuttgart #
# therefore editing the shell commands as GUI                          #
#                                                                      #
# by: Andre Jaenisch                                                   #
# license: GPL                                                         #
########################################################################

# Import module for accessing the shell
import subprocess

# Import all the headers for Qt and KDE
from PyQt4.QtCore import *
from PyQt4.QtGui import *
#from PyKDE4.kdecore import *
#from PyKDE4.kdeui import *
from PyKDE4.plasma import Plasma
from PyKDE4 import plasmascript
#from PyQt4 import QtCore, QtGui

class SpaceLeftApplet(plasmascript.Applet):
	# constructor
	def __init__(self, parent,  args=None):
		plasmascript.Applet.__init__(self,  parent)

	def init(self):
		# disable settings dialog
		self.setHasConfigurationInterface(False)
		self.setAspectRatioMode(Plasma.Square)
		
		# Set background
		self.theme = Plasma.Svg(self)
        
        # Next, we add a background to the applet using a SVG image provided by
        # the standard Plasma theme. We do so by creating an instance of Plasma.
        # Svg, assigning it to self.theme, and then specifying the SVG graphic we
        # want to use via self.setImagePath(). This way the applet will use the
        # standard "background" SVG provided by the "widgets" directory of our
        # current Plasma theme. We can also use relative paths or absolute paths
        # to SVGs of our choice, should we need to.
		self.theme.setImagePath("widgets/background")
		self.setBackgroundHints(Plasma.Applet.DefaultBackground)
		
		# Create layout
		self.layout = QGraphicsLinearLayout(Qt.Horizontal, self.applet)
		self.resize(320, 100)
		
		# Set timer in ms (1000ms = 1s)
		#self.startTimer(1000)
		
		# Get the content		
		self.getQuota()
		
	#def timerEvent(self,event):
        #self.connectToEngine()
		#self.getQuota()
		#pass
		
	def getQuota(self):
		# Extracting the remaining quota using a shell command
		quota = subprocess.Popen(['fs','quota','.'],stdout=subprocess.PIPE)
		space_left = quota.stdout.read().split(' ')[0]
				
		# Printing the result into the widget
		label = Plasma.Label(self.applet)
		content = "You have %s space in use." %space_left
		label.setText(content)
		print(content)
		self.update()
		self.layout.addItem(label)
	
# Tell Plasma how to get this class
def CreateApplet(parent):
	return SpaceLeftApplet(parent)

# Read more here:
# plasmaengineexplorer
# plasmoidviewer space-left
# Data-engine python plasmoid
# http://techbase.kde.org/Development/Tutorials/Plasma/Python/Using_DataEngines
# http://server.ericsbinaryworld.com/blog/2012/02/15/developing-my-first-plasmoid-the-data-engine-in-python/
