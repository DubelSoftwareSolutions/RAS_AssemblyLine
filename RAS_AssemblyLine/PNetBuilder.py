import yaml
from PT_Simulator import *

class PNetBuilder:
    @classmethod
    def build(cls, fname):
        LineSimulator = PT_Simulator()
        with open(fname) as f:
            configuration = yaml.load(f)

        MachinesBufferCapacities = cls.loadMachines(cls, configuration)

        print(MachinesBufferCapacities)

    def loadMachines(self, configuration):
        machines_buffer_capacities = []
        machines = configuration['machines']

        for machine in machines:
            machines_buffer_capacities.append(machines[machine]['capacity'])

        return machines_buffer_capacities