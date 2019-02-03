import time
import snakes.plugins
snakes.plugins.load('gv', 'snakes.nets', 'nets')
from nets import *
from PT_Simulator import *

if __name__ == "__main__":
    LineSimulator = PT_Simulator()
    BufferCapacity = [1,1]
    ProcessOperations = [[0, 1]]
    OperationDuration = [[3, 4]]
    PTnet = LineSimulator.buildLinePTModel(BufferCapacity,ProcessOperations, OperationDuration)
    
    while(True):
        print(LineSimulator.enabledTransitions())
        print(LineSimulator.net.get_marking())
        if(len(LineSimulator.enabledTransitions()) > 0):
            LineSimulator.fireTransition(LineSimulator.enabledTransitions()[-1].name)
        time.sleep(1)

    PTnet.draw('OneProcessLineParametrised.png')