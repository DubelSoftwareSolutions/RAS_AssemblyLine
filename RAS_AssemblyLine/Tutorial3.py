import snakes.plugins
snakes.plugins.load('gv', 'snakes.nets', 'nets')
from nets import *
n = PetriNet('Tutorial Net')
n.add_place(Place('p0', ['p0tok']))
n.add_place(Place('p1', ['p1tok']))
n.add_place(Place('p2', []))

n.add_transition(Transition('t0'))
n.add_input('p0','t0',Value('p0tok'))
n.add_input('p1','t0',Value('p1tok'))
n.add_output('p2','t0',Value(['p0tok','p1tok']))

n.add_transition(Transition('t1'))
n.add_input('p2','t1',Value(['p0tok','p1tok']))
n.add_output('p0','t1',Value('p0tok'))
n.add_output('p1','t1',Value('p1tok'))

for i in range(0,5):
    if (not n.transition('t0').modes()):
        n.transition('t1').fire(Substitution())
    else:
        n.transition('t0').fire(Substitution())
    print(n.get_marking())
