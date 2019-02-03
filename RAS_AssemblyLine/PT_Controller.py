import time
import snakes.plugins
snakes.plugins.load('gv', 'snakes.nets', 'nets')
from nets import *
from PT_Simulator import *
import numpy

class PT_Controller(object):

    def __init__(self):
        self.ProcessFinishPriority = 100
        self.OperationFinishPriority = 200
        self.OperationBeginPriority = 300
        self.OperationPreparePriority = 400

    def ExecuteHighestPriority(self, Simulator):
        Transitions = Simulator.enabledTransitions()
        TransitionPriorities = [0] * len(Transitions)
        for i in range(0,len(Transitions)):
            if("_O" not in Transitions[i].name):
                TransitionPriorities[i] = self.ProcessFinishPriority
            else:
                if("Finish" in Transitions[i].name):
                    TransitionPriorities[i] = self.OperationFinishPriority
                elif("Begin" in Transitions[i].name):
                    TransitionPriorities[i] = self.OperationBeginPriority
                elif("Prepare" in Transitions[i].name):
                    TransitionPriorities[i] = self.OperationPreparePriority
                TransitionPriorities[i] += int(Transitions[i].name[4])*1
            #TransitionPriorities[i] += int(Transitions[i].name[1])*10
        TransitionToFire = Transitions[numpy.argmin(TransitionPriorities)].name
        print("Transition To Fire: "+TransitionToFire)
        #input("Press Enter to continue...")
        Simulator.fireTransition(TransitionToFire)

    def HandleDeadlock(self, Simulator):
        input("Press Enter to continue...")
        sys.exit(-1)