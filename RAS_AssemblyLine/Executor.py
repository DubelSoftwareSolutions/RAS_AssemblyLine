import time
import sys
from PT_NetBuilder import *
from PT_Simulator import *

drawings = 'drawings/'
def main():
    if len(sys.argv) < 2:
        print("Configuration name is required")
        config = 'example'
    else:
        config = sys.argv[1]

    LineSimulator = PT_Simulator()

    PTNet = PT_NetBuilder.build('config/' + config + '.yaml', LineSimulator)
    while(True):
       print(LineSimulator.enabledTransitions())
       print(LineSimulator.net.get_marking())
       if(len(LineSimulator.enabledTransitions()) > 0):
           LineSimulator.fireTransition(LineSimulator.enabledTransitions()[-1].name)
       input("Press Enter to continue...")


if __name__ == '__main__':
    main()