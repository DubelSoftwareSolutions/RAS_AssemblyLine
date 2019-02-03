import yaml
import sys
from PT_NetBuilder import *
from PT_Simulator import *


def main():
    if len(sys.argv) < 2:
        print("Configuration name is required")
        sys.exit(1)

    LineSimulator = PT_Simulator()

    # FIXME wrong array types
    PTNet = PT_NetBuilder.build('config/' + sys.argv[1] + '.yaml', LineSimulator)
    LineSimulator.enabledTransitions()
    print(LineSimulator.enabledTransitions())



if __name__ == '__main__':
    main()