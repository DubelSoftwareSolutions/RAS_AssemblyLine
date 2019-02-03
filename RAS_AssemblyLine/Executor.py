import time
import sys
import numpy
from PT_NetBuilder import *
from PT_Simulator import *
from PT_Controller import *

drawings = 'drawings/'
def main():
    if len(sys.argv) < 2:
        print("Configuration name is required")
        config = 'example'
    else:
        config = sys.argv[1]

    LineSimulator = PT_Simulator()
    LineController = PT_Controller()

    PTNet = PT_NetBuilder.build('config/' + config + '.yaml', LineSimulator)
    PTNet.draw(drawings + 'OneProcessLineParametrised.png')
    deadlockTimer = time.time()
    print(LineSimulator.enabledTransitions())
    print(LineSimulator.net.get_marking())
    while(True):
       #input("Press Enter to continue...")
       if(len(LineSimulator.enabledTransitions()) > 0):
           deadlockTimer = time.time()
           LineController.ExecuteHighestPriority(LineSimulator)
           print(LineSimulator.enabledTransitions())
           print(LineSimulator.net.get_marking())
       else:
           if(time.time() - deadlockTimer > numpy.max(LineSimulator.OperationDuration) + 2):
               print("DEADLOCK OCCURED")
               LineController.HandleDeadlock(LineSimulator)


if __name__ == '__main__':
    main()