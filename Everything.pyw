import voicemeeter
import sys
from Lib import MUTEALL, RESTARTENGINE, STRIP0, STRIP1, STRIP5, STRIP6, STRIP7

# Parameters passed to the script when script is started
muteall = "muteAll"
restartEngine = "restartEngine"
strip0 = "strip0"
strip1 = "strip1"
strip5 = "strip5"
strip6 = "strip6"
strip7 = "strip7"

x = sys.argv

# referr to the module for parameters to pass
for a in x:
    if a == muteall:
        MUTEALL.muteAll()
    if a == restartEngine:
        RESTARTENGINE.restart()
    if a == strip0:
        STRIP0.strip0(x[2], x[3])
    if a == strip1:
        STRIP1.strip1(x[2], x[3])
    if a == strip5:
        STRIP5.strip5(x[2], x[3])
    if a == strip6:
        STRIP6.strip6(x[2], x[3])
    if a == strip7:
        STRIP7.strip7(x[2], x[3])
