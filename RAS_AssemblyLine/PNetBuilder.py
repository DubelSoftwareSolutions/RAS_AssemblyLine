import yaml
from PT_Simulator import *

class PNetBuilder:
    MachinesBufferCapacities = []
    OperationOrders = []
    NumberOfParts = []

    @classmethod
    def build(cls, fname):
        LineSimulator = PT_Simulator()
        with open(fname) as f:
            configuration = yaml.load(f)

        cls.loadMachines(configuration)
        cls.loadProcesses(configuration)

        print(cls.MachinesBufferCapacities)
        print(cls.OperationOrders)
        print(cls.NumberOfParts)

    @classmethod
    def loadMachines(cls, configuration):
        cls.MachinesBufferCapacities = []
        Machines = configuration['machines']

        for machine in Machines:
            cls.MachinesBufferCapacities.append(Machines[machine]['capacity'])

        return cls.MachinesBufferCapacities

    @classmethod
    def loadProcesses(cls, configuration):
        cls.OperationOrders = []
        cls.NumberOfParts = []
        Processes = configuration['processes']

        for process in Processes:
            order = []
            cls.NumberOfParts.append(Processes[process]['number_of_parts'])
            for operation in Processes[process]['order']:
                order.append(operation)

            cls.OperationOrders.append(order)


