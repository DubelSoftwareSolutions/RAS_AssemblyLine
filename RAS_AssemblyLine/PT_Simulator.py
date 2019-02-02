import snakes.plugins
snakes.plugins.load('gv', 'snakes.nets', 'nets')
from nets import *

class PT_Simulator(object):
    
    def __init__(self):
        self.net = PetriNet('MultiProcessAssemblyLine')
        self.TransitionFired = 0
        self.TransitionDisabled = 1

    def buildLinePTModel(self, BufferCapacity, ProcessOperations):
        numberOfRobots = 1
        numberOfMachines = len(BufferCapacity)
        numberOfProcesses = len(ProcessOperations)
        net = self.net
        for i in range(0, numberOfRobots):
            net.add_place(Place('Robot'+str(i), [1]))
        for i in range(0, numberOfMachines):
            bufferMarking = [1] * BufferCapacity[i]
            net.add_place(Place('Machine'+str(i),[1]))
            net.add_place(Place('Buffer'+str(i),bufferMarking))
    
    
        for i in range(0, len(ProcessOperations)):
            for j in range(0, len(ProcessOperations[i])):
                net.add_place(Place('P'+str(i)+'_O'+str(j)+'_Ready',[]))
                net.add_place(Place('P'+str(i)+'_O'+str(j)+'_InProgress',[]))
                net.add_place(Place('P'+str(i)+'_O'+str(j)+'_Finished',[]))
        
                net.add_transition(Transition('P'+str(i)+'_O'+str(j)+'_Prepare'))
                net.add_input('Buffer'+str(ProcessOperations[i][j]),'P'+str(i)+'_O'+str(j)+'_Prepare',Value(1))
                net.add_input('Robot0','P'+str(i)+'_O'+str(j)+'_Prepare',Value(1))
                net.add_output('P'+str(i)+'_O'+str(j)+'_Ready','P'+str(i)+'_O'+str(j)+'_Prepare',Value(1))
                net.add_output('Robot0','P'+str(i)+'_O'+str(j)+'_Prepare',Value(1))
                if(j > 0):
                    net.add_input('P'+str(i)+'_O'+str(j-1)+'_Finished','P'+str(i)+'_O'+str(j)+'_Prepare',Value(1))
                    net.add_output('Buffer'+str(ProcessOperations[i][j-1]),'P'+str(i)+'_O'+str(j)+'_Prepare',Value(1))
        
                net.add_transition(Transition('P'+str(i)+'_O'+str(j)+'_Begin'))
                net.add_input('P'+str(i)+'_O'+str(j)+'_Ready','P'+str(i)+'_O'+str(j)+'_Begin',Value(1))
                net.add_input('Machine'+str(ProcessOperations[i][j]),'P'+str(i)+'_O'+str(j)+'_Begin',Value(1))
                net.add_output('P'+str(i)+'_O'+str(j)+'_InProgress','P'+str(i)+'_O'+str(j)+'_Begin',Value(1))
        
                net.add_transition(Transition('P'+str(i)+'_O'+str(j)+'_Finish'))
                net.add_input('P'+str(i)+'_O'+str(j)+'_InProgress','P'+str(i)+'_O'+str(j)+'_Finish',Value(1))
                net.add_output('Machine'+str(ProcessOperations[i][j]),'P'+str(i)+'_O'+str(j)+'_Finish',Value(1))
                net.add_output('P'+str(i)+'_O'+str(j)+'_Finished','P'+str(i)+'_O'+str(j)+'_Finish',Value(1))
    
            net.add_transition(Transition('P'+str(i)+'_Finish'))
            net.add_input('P'+str(i)+'_O'+str(len(ProcessOperations[i])-1)+'_Finished','P'+str(i)+'_Finish',Value(1))
            net.add_input('Robot0','P'+str(i)+'_Finish',Value(1))
            net.add_output('Buffer'+str(ProcessOperations[i][-1]),'P'+str(i)+'_Finish',Value(1))
            net.add_output('Robot0','P'+str(i)+'_Finish',Value(1))

        return net

    def fireTransition(self, transitionName):
        net = self.net
        if(len(net.transition(transitionName).modes()) > 0):
            net.transition(transitionName).fire(Substitution())
            return self.TransitionFired
        else:
            return self.TransitionDisabled
            
    def enabledTransitions(self):
        EnabledTransitions = []
        for transition in self.net.transition():
            if(len(transition.modes()) > 0):
                EnabledTransitions.extend([transition])
        return EnabledTransitions





