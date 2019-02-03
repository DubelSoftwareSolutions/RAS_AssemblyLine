import yaml
import sys
from PNetBuilder import *
from PT_Simulator import *


def main():
    if len(sys.argv) < 2:
        print("Configuration name is required")
        sys.exit(1)

    LineSimulator = PT_Simulator()

    # FIXME wrong array types
    PTNet = PNetBuilder.build('config/' + sys.argv[1] + '.yaml', LineSimulator)
    print(LineSimulator.enabledTransitions())



if __name__ == '__main__':
    main()