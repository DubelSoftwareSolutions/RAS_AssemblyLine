import snakes.plugins
snakes.plugins.load('gv', 'snakes.nets', 'nets')
from nets import *
from PT_Simulator import *

if __name__ == "__main__":
    LineSimulator = PT_Simulator()
    BufferCapacity = [2,1]
    ProcessOperations = [[0, 1]]
    PTnet = LineSimulator.buildLinePTModel(BufferCapacity,ProcessOperations)
    print(PTnet.get_marking())
    PTnet.draw('OneProcessLineParametrised.png')