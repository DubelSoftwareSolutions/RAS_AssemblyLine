import snakes.plugins
snakes.plugins.load('gv', 'snakes.nets', 'nets')
from nets import *
n = PetriNet('Tutorial Net')
n.add_place(Place('p0', ['dupa']))
n.add_place(Place('p1', ['kupa']))
n.add_place(Place('p2', []))
n.add_place(Place('p3', []))

n.add_transition(Transition('t0'))
n.add_input('p0','t0',Value('dupa'))
n.add_input('p1','t0',Value('kupa'))
n.add_output('p2','t0',Value('dupa'))
n.add_output('p3','t0',Value('kupa'))

n.draw('TutorialNet.png')
print(n.transition('t0').modes())
n.transition('t0').fire(Substitution())
n.draw('TutorialNetfire1.png')
print(n.transition('t0').modes())

