import snakes.plugins
snakes.plugins.load('gv', 'snakes.nets', 'nets')
from nets import *
n = PetriNet('Tutorial Net')
n.add_place(Place('p0', [1]))
n.add_place(Place('p1', []))
n.add_transition(Transition('t0',Expression('x>0')))
n.add_input('p0','t0',Variable('x'))
n.add_output('p1','t0',Variable('x'))

n.draw('TutorialNet.png')
print(n.transition('t0').modes())
n.transition('t0').fire(Substitution(x=1))
print(n.place('p0').tokens)
n.draw('TutorialNetfire1.png')