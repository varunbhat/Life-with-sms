import sys
import time
from PyQt4.QtCore import *
from PyQt4.QtGui import *

app = QApplication(sys.argv)


due = QTime.currentTime()
message = "Alert!"
if len(sys.argv) < 2:
    raise ValueError
hours, mins = sys.argv[1].split(":")
due = QTime(int(hours), int(mins))
if not due.isValid():
    raise ValueError
if len(sys.argv) > 2:
    message = " ".join(sys.argv[2:])
print "here"
#except ValueError:
#print "error happened"
#message = "Usage: alert.pyw HH:MM [optional message]" # 24hr clock
