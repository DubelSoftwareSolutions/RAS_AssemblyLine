import matplotlib.pyplot as plt

def display(file, machines):
    f = open(file, 'r')

    data = f.read()
    lines = data.split("\n")
    tr = []
    max_time = 0
    for line in lines:
        tr.append(line.split('_'))

    machine_times = []
    for i in range(1, machines):
        machine_times.append([])

    for i in range(0, len(tr)):
        if(len(tr[i]) > 4 and tr[i][2] == "Begin"):
            max_time = max(max_time, int(tr[i][3]))
            for j in range(i, len(tr)):
                if(tr[i][0] == tr[j][0] and tr[i][0] == tr[j][0] and
                        tr[j][2] == "Finish"):
                    machine_times[int(tr[j][4])].append([tr[i][3], tr[j][3]])
                    break

    print(machine_times)
    fig, ax = plt.subplots()

    n = []
    y = []

    for m in range(0, machines - 1):
        n.append('Machine ' + str(m))
        y.append(m*10+5)
        v = []
        for j in range(0, len(machine_times[m])-1):
            s_time = int(machine_times[m][j][0])
            e_time = int(machine_times[m][j][1])
            v.append([s_time, e_time - s_time])

        ax.broken_barh(v,[m*10,9])

    ax.set_ylim(5, machines*10+5)
    ax.set_xlim(0, max_time+5)
    ax.set_xlabel('seconds since start')
    ax.set_yticks(y)
    ax.set_yticklabels(n)
    ax.grid(True)
    plt.show()