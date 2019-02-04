import time
import sys
import numpy
from PT_NetBuilder import *
from PT_Simulator import *
from PT_Controller import *
from SimPlot import *

drawings = 'drawings/'
def main():
    if len(sys.argv) < 2:
        print("Configuration name is required")
        config = 'example'
    else:
        config = sys.argv[1]

    display("output/sim_2019_02_03__22_52_52.txt", 4)
    sys.exit()

    LineSimulator = PT_Simulator()
    LineController = PT_Controller()

    PTNet = PT_NetBuilder.build('config/' + config + '.yaml', LineSimulator)
    PTNet.draw(drawings + 'OneProcessLineParametrised.png')
    deadlockTimer = time.time()
    while(True):
       #input("Press Enter to continue...")
       print("")
       print(LineSimulator.enabledTransitions())
       print(LineSimulator.net.get_marking())
       if(len(LineSimulator.enabledTransitions()) > 0):
           deadlockTimer = time.time()
           LineController.ExecuteHighestPriority(LineSimulator)
       else:
           if(time.time() - deadlockTimer > numpy.max(LineSimulator.OperationDuration) + 2):
               print("DEADLOCK OCCURED")
               LineController.HandleDeadlock(LineSimulator)
               display(LineSimulator.OutputFilePath, len(LineSimulator.BufferCapacity))
       time.sleep(1)
    display(LineSimulator.OutputFilePath)


if __name__ == '__main__':
    main()