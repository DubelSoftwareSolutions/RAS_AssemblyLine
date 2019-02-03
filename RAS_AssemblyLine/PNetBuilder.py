import yaml
from PT_Simulator import *

class PNetBuilder:
    MachinesBufferCapacities = []
    OperationOrders = []
    NumberOfParts = []
    RquiredMachines = []
    ExecutionTimes = []

    @classmethod
    def build(cls, fname, simulator):
        cls.load(fname)

        print(cls.MachinesBufferCapacities)
        print(cls.OperationOrders)
        print(cls.NumberOfParts)

        print(cls.RquiredMachines)
        print(cls.ExecutionTimes)

        return simulator.buildLinePTModel(cls.MachinesBufferCapacities, cls.OperationOrders, cls.ExecutionTimes)

    @classmethod
    def load(cls, fname):
        with open(fname) as f:
            configuration = yaml.load(f)

        cls.loadMachines(configuration)
        cls.loadProcesses(configuration)
        cls.loadOperations(configuration)

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


    @classmethod
    def loadOperations(cls, configuration):
        cls.RquiredMachines = []
        cls.ExecutionTimes = []
        Operations = configuration['operations']

        for operation in Operations:
            cls.RquiredMachines.append(Operations[operation]['required_machine'])
            cls.ExecutionTimes.append(Operations[operation]['execution_time'])
