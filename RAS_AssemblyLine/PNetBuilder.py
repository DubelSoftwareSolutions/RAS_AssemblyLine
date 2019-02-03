import yaml
from PT_Simulator import *

class PNetBuilder:
    @classmethod
    def build(cls, fname):
        LineSimulator = PT_Simulator()
        with open(fname) as f:
            configuration = yaml.load(f)

        MachinesBufferCapacities = cls.loadMachines(cls, configuration)
        orders = cls.loadProcessOrders(cls, configuration)

        print(MachinesBufferCapacities)
        print(orders)

    def loadMachines(self, configuration):
        machines_buffer_capacities = []
        machines = configuration['machines']

        for machine in machines:
            machines_buffer_capacities.append(machines[machine]['capacity'])

    def loadProcessOrders(self, configuration):
        OperationOrders = []

        Processes = configuration['processes']

        for process in Processes:
            order = []
            for operation in Processes[process]['order']:
                order.append(operation)

            OperationOrders.append(order)

        return OperationOrders