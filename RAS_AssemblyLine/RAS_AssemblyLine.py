import snakes.plugins
snakes.plugins.load('gv', 'snakes.nets', 'nets')
from nets import *
n = PetriNet('Tutorial Net')
n.add_place(Place('p0', [1,1,1]))
n.add_place(Place('p1', []))

n.add_transition(Transition('t0'))
n.add_input('p0','t0',Value(1))
n.add_output('p1','t0',Value(1))

n.add_transition(Transition('t1'))
n.add_input('p1','t1',Value(1))
n.add_output('p0','t1',Value(1))


n.draw('TutorialNet.png')
print(n.transition('t0').modes())
n.transition('t0').fire(Substitution())
n.draw('TutorialNetfire1.png')
n.transition('t0').fire(Substitution())
n.draw('TutorialNetfire2.png')
n.transition('t1').fire(Substitution())
n.draw('TutorialNetfire3.png')
n.transition('t0').fire(Substitution())
n.draw('TutorialNetfire4.png')
