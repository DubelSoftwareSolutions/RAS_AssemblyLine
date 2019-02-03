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
    LineSimulator.enabledTransitions()
    print(LineSimulator.enabledTransitions())
    LineSimulator.fireTransition(LineSimulator.enabledTransitions()[0].name)
    time_start = time.time()
    print(LineSimulator.enabledTransitions())
    # while(time.time() - time_start <= OperationDuration[0][0]):
    #     dupa = 0
    print(LineSimulator.enabledTransitions())
    PTNet.draw(drawings+'OneProcessLineParametrised.png')


if __name__ == '__main__':
    main()