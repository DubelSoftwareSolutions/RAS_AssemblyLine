import snakes.plugins
snakes.plugins.load('gv', 'snakes.nets', 'nets')
from nets import *
net = PetriNet('Tutorial Net')

net.add_place(Place('Robot', [1]))
net.add_place(Place('Machine0',[1]))
net.add_place(Place('Machine1',[1]))
net.add_place(Place('Buffer0',[1,1]))
net.add_place(Place('Buffer1',[1]))

net.add_place(Place('P0_O0_Ready',[]))
net.add_place(Place('P0_O0_InProgress',[]))
net.add_place(Place('P0_O0_Finished',[]))

net.add_place(Place('P0_O1_Ready',[]))
net.add_place(Place('P0_O1_InProgress',[]))
net.add_place(Place('P0_O1_Finished',[]))

#operation0

net.add_transition(Transition('P0_O0_Prepare'))
net.add_input('Buffer0','P0_O0_Prepare',Value(1))
net.add_input('Robot','P0_O0_Prepare',Value(1))
net.add_output('P0_O0_Ready','P0_O0_Prepare',Value(1))
net.add_output('Robot','P0_O0_Prepare',Value(1))

net.add_transition(Transition('P0_O0_Begin'))
net.add_input('P0_O0_Ready','P0_O0_Begin',Value(1))
net.add_input('Machine0','P0_O0_Begin',Value(1))
net.add_output('P0_O0_InProgress','P0_O0_Begin',Value(1))

net.add_transition(Transition('P0_O0_Finish'))
net.add_input('P0_O0_InProgress','P0_O0_Finish',Value(1))
net.add_output('Machine0','P0_O0_Finish',Value(1))
net.add_output('P0_O0_Finished','P0_O0_Finish',Value(1))

#operation1

net.add_transition(Transition('P0_O1_Prepare'))
net.add_input('P0_O0_Finished','P0_O1_Prepare',Value(1))
net.add_input('Buffer1','P0_O1_Prepare',Value(1))
net.add_input('Robot','P0_O1_Prepare',Value(1))
net.add_output('P0_O1_Ready','P0_O1_Prepare',Value(1))
net.add_output('Buffer0','P0_O1_Prepare',Value(1))
net.add_output('Robot','P0_O1_Prepare',Value(1))

net.add_transition(Transition('P0_O1_Begin'))
net.add_input('P0_O1_Ready','P0_O1_Begin',Value(1))
net.add_input('Machine1','P0_O1_Begin',Value(1))
net.add_output('P0_O1_InProgress','P0_O1_Begin',Value(1))

net.add_transition(Transition('P0_O1_Finish'))
net.add_input('P0_O1_InProgress','P0_O1_Finish',Value(1))
net.add_output('Machine1','P0_O1_Finish',Value(1))
net.add_output('P0_O1_Finished','P0_O1_Finish',Value(1))

#finish

net.add_transition(Transition('P0_Finish'))
net.add_input('P0_O1_Finished','P0_Finish',Value(1))
net.add_input('Robot','P0_Finish',Value(1))
net.add_output('Buffer1','P0_Finish',Value(1))
net.add_output('Robot','P0_Finish',Value(1))

net.draw('OneProcessLine.png')