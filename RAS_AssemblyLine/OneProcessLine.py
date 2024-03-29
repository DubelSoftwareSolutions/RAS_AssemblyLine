import snakes.plugins
snakes.plugins.load('gv', 'snakes.nets', 'nets')
from nets import *
net = PetriNet('Tutorial Net')

numberOfMachines = 2
numberOfRobots = 1
numberOfProcesses = 1
ProcessOperations = [[0, 1]]

for i in range(0, numberOfRobots):
    net.add_place(Place('Robot'+str(i), [1]))
for i in range(0, numberOfMachines):
    net.add_place(Place('Machine'+str(i),[1]))
    net.add_place(Place('Buffer'+str(i),[1,1]))


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

net.draw('OneProcessLineParametrised.png')