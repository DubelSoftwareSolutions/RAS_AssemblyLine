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
    print(LineSimulator.enabledTransitions())
    LineSimulator.fireTransition(LineSimulator.enabledTransitions()[0].name)
    time_start = time.time()
    print(LineSimulator.enabledTransitions())
    while(time.time() - time_start <= OperationDuration[0][0]):
        dupa = 0
    print(LineSimulator.enabledTransitions())
    PTnet.draw('OneProcessLineParametrised.png')