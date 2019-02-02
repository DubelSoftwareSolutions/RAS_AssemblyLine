import snakes.plugins
snakes.plugins.load('gv', 'snakes.nets', 'nets')
from nets import *
from PT_Simulator import *

if __name__ == "__main__":
    LineSimulator = PT_Simulator()
    BufferCapacity = [1,1]
    ProcessOperations = [[0, 1]]
    OperationDuration = [[10, 20]]
    PTnet = LineSimulator.buildLinePTModel(BufferCapacity,ProcessOperations, OperationDuration)
    print(LineSimulator.enabledTransitions())
    LineSimulator.fireTransition(LineSimulator.enabledTransitions()[0].name)
    LineSimulator.fireTransition(LineSimulator.enabledTransitions()[0].name)
    print(LineSimulator.enabledTransitions())
    PTnet.draw('OneProcessLineParametrised.png')