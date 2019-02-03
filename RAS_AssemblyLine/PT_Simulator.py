import time
import snakes.plugins
snakes.plugins.load('gv', 'snakes.nets', 'nets')
from nets import *

class PT_Simulator(object):
    
    def __init__(self):
        self.net = PetriNet('MultiProcessAssemblyLine')
        self.TransitionFired = 0
        self.TransitionDisabled = 1
        self.ProcessOperations = []
        self.OperationDuration = []
        self.ProgressTimers = []

    def buildLinePTModel(self, BufferCapacity, ProcessOperations, OperationDuration):
        numberOfRobots = 1
        numberOfMachines = len(BufferCapacity)
        numberOfProcesses = len(ProcessOperations)
        self.ProcessOperations = ProcessOperations
        self.OperationDuration = OperationDuration
        self.ProgressTimers = [[0] * len(ProcessOperations[0])] * len(ProcessOperations)
        net = self.net
        for i in range(0, numberOfRobots):
            net.add_place(Place('Robot'+str(i), ['R']))
        for i in range(0, numberOfMachines):
            bufferMarking = list(range(0,numberOfProcesses)) * BufferCapacity[i]
            net.add_place(Place('Machine'+str(i),['M'+str(i)]))
            net.add_place(Place('Buffer'+str(i),bufferMarking))
    
    
        for i in range(0, len(ProcessOperations)):
            for j in range(0, len(ProcessOperations[i])):
                if(j == 0):
                    Tokens = []
                else:
                    Tokens = []
                net.add_place(Place('P'+str(i)+'_O'+str(j)+'_Ready',Tokens))
                net.add_place(Place('P'+str(i)+'_O'+str(j)+'_InProgress',[]))
                net.add_place(Place('P'+str(i)+'_O'+str(j)+'_Finished',[]))
        
                net.add_transition(Transition('P'+str(i)+'_O'+str(j)+'_Prepare'))
                net.add_input('Buffer'+str(ProcessOperations[i][j]),'P'+str(i)+'_O'+str(j)+'_Prepare',Value(i))
                net.add_input('Robot0','P'+str(i)+'_O'+str(j)+'_Prepare',Value('R'))
                net.add_output('P'+str(i)+'_O'+str(j)+'_Ready','P'+str(i)+'_O'+str(j)+'_Prepare',Value(i))
                net.add_output('Robot0','P'+str(i)+'_O'+str(j)+'_Prepare',Value('R'))
                if(j > 0):
                    net.add_input('P'+str(i)+'_O'+str(j-1)+'_Finished','P'+str(i)+'_O'+str(j)+'_Prepare',Value(i))
                    net.add_output('Buffer'+str(ProcessOperations[i][j-1]),'P'+str(i)+'_O'+str(j)+'_Prepare',Value(i))
        
                net.add_transition(Transition('P'+str(i)+'_O'+str(j)+'_Begin'))
                net.add_input('P'+str(i)+'_O'+str(j)+'_Ready','P'+str(i)+'_O'+str(j)+'_Begin',Value(i))
                net.add_input('Machine'+str(ProcessOperations[i][j]),'P'+str(i)+'_O'+str(j)+'_Begin',Value('M'+str(ProcessOperations[i][j])))
                net.add_output('P'+str(i)+'_O'+str(j)+'_InProgress','P'+str(i)+'_O'+str(j)+'_Begin',Value(i))
        
                net.add_transition(Transition('P'+str(i)+'_O'+str(j)+'_Finish'))
                net.add_input('P'+str(i)+'_O'+str(j)+'_InProgress','P'+str(i)+'_O'+str(j)+'_Finish',Value(i))
                net.add_output('Machine'+str(ProcessOperations[i][j]),'P'+str(i)+'_O'+str(j)+'_Finish',Value('M'+str(ProcessOperations[i][j])))
                net.add_output('P'+str(i)+'_O'+str(j)+'_Finished','P'+str(i)+'_O'+str(j)+'_Finish',Value(i))
    
            net.add_transition(Transition('P'+str(i)+'_Finish'))
            net.add_input('P'+str(i)+'_O'+str(len(ProcessOperations[i])-1)+'_Finished','P'+str(i)+'_Finish',Value(i))
            net.add_input('Robot0','P'+str(i)+'_Finish',Value('R'))
            net.add_output('Buffer'+str(ProcessOperations[i][-1]),'P'+str(i)+'_Finish',Value(i))
            net.add_output('Robot0','P'+str(i)+'_Finish',Value('R'))

        return net

    def fireTransition(self, transitionName):
        net = self.net
        if(len(net.transition(transitionName).modes()) > 0):
            net.transition(transitionName).fire(Substitution())
            if( "Begin" in transitionName):
                placeName = transitionName.replace("Begin","InProgress")
                net.place(placeName).empty()
                self.ProgressTimers[int(placeName[1])][int(placeName[4])] = time.time()
            return self.TransitionFired
        else:
            return self.TransitionDisabled
            
    def enabledTransitions(self):
        EnabledTransitions = []
        for i in range(0,len(self.ProgressTimers)):
            for j in range(0,len(self.ProgressTimers[i])):
                if(self.ProgressTimers[i][j] > 0):
                    currentTime = time.time()
                    if(currentTime - self.ProgressTimers[i][j] >= self.OperationDuration[i][j]):
                        placeName = 'P'+str(i)+'_O'+str(j)+'_InProgress'
                        self.net.place(placeName).add(i)
                        self.ProgressTimers[i][j] = 0

        for transition in self.net.transition():
            if(len(transition.modes()) > 0):
                EnabledTransitions.extend([transition])
        return EnabledTransitions