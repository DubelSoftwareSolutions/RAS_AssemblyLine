import yaml
import sys


def main():
    if len(sys.argv) < 2:
        print("Configuration name is required")
        sys.exit(1)

    with open('config/' + sys.argv[1] + '.yaml') as f:
        configuration = yaml.load(f)

    operations = configuration['operations']

    for operation in operations:
        print(operations[operation])








if __name__ == '__main__':
    main()