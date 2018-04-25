__author__ = "Alper Ozaydin"

#dasher_spotify

import os
import commands

def dasher_spotify():
	status, output = commands.getstatusoutput("spotify p")
	print output


dasher_spotify()