import matplotlib.pyplot as plt
from utils import roundup
import random
import math
from config import config as cfg


def rr_plot(list_of_processes, timestamp):
    width_xaxis = []
    for process in list_of_processes:
        width_xaxis.append(process.termination_time)
    width_value = max(width_xaxis)
    height_value = cfg["RR"]["RR_PROCESS_RANGE"] * 5 + 5

    WIDTH = math.ceil((width_value + 150) / 50)
    HEIGHT = math.ceil((height_value + 150) / 50)
    BAR_HEIGHT = 2

    fig, gnt = plt.subplots(figsize=(WIDTH, HEIGHT))

    plt.title(f'GANNT PLOT FOR {cfg["RR"]["RR_PROCESS_RANGE"]} PROCESSES, RR, '
              f'QUANTUM {cfg["RR"]["RR_QUANTUM"]} [MS]')

    gnt.set_ylim(0, height_value)
    gnt.set_xlim(0, roundup(width_value + 15))

    gnt.set_xlabel('Time[ms]')
    gnt.set_ylabel('Process')

    gnt.set_yticks([i for i in range(5, cfg["RR"]["RR_PROCESS_RANGE"] * 5 +
                                     5, 5)])
    gnt.invert_yaxis()

    gnt.grid(True)
    gnt.set_axisbelow(True)

    names = []
    # mark times
    for index, process in enumerate(list_of_processes):
        names.append("P" + str(process.name))
        for interval in process.waiting_list:
            gnt.broken_barh([(interval[0], interval[1] - interval[0])],
                            ((index * 5 + 5) - BAR_HEIGHT / 2,
                             BAR_HEIGHT),
                            facecolors='#8e8888', label='waiting time')
        for interval in process.working_list:
            gnt.broken_barh([(interval[0], interval[1] - interval[0])],
                            ((index * 5 + 5) - BAR_HEIGHT / 2,
                             BAR_HEIGHT),
                            facecolors='#00ff00', label='burst time')
        gnt.annotate(f'{process.termination_time}',
                     xy=(
                         process.termination_time,
                         index * 5 + 5 + BAR_HEIGHT / 2),
                     xytext=(BAR_HEIGHT * 10, 5),
                     xycoords='data',
                     textcoords='offset pixels', ha='center', va='center')

    gnt.set_yticklabels(names)

    # fix legend
    hand, labl = gnt.get_legend_handles_labels()
    handout = []
    lablout = []
    for h, l in zip(hand, labl):
        if l not in lablout:
            lablout.append(l)
            handout.append(h)
    gnt.legend(handout, lablout, prop={'size': 6})

    title = "CHART_RR_" + timestamp + ".png"
    sub = timestamp + "/"
    plt.savefig(sub + title)


randomhex = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c',
             'd', 'e', 'f']


def fcfs_plot(list_of_processes, timestamp):
    width_xaxis = []
    for process in list_of_processes:
        width_xaxis.append(process.termination_time)
    width_value = max(width_xaxis)
    plt.style.use('default')

    WIDTH = math.ceil((width_value + 150) / 50)
    HEIGHT = math.ceil((len(list_of_processes)*16)/100)
    fig, gnt = plt.subplots(figsize=(WIDTH, max(HEIGHT, 4)))

    processes = cfg["FCFS"]["FCFS_PROCESS_RANGE"]
    if cfg["SUB"]["USE_RR_TO_FCFS"]:
        processes = cfg["RR"]["RR_PROCESS_RANGE"]

    plt.title(f'GANNT PLOT FOR {processes} PROCESSES, FCFS')

    # os Y - wysokosc
    gnt.set_ylim(0, 4)

    # os X - szerokosc w oparciu o najdluzej wykonywany proces
    gnt.set_xlim(0, roundup(width_value))

    # tytuly osi X i Y
    gnt.set_xlabel('Time[ms]')
    # gnt.set_ylabel('Process')
    gnt.set_yticks([2])
    gnt.set_yticklabels([' '])

    gnt.invert_yaxis()

    gnt.grid(True)
    gnt.set_axisbelow(True)

    for index, process in enumerate(list_of_processes):
        res_0 = process.working_list[0]
        res_1 = process.working_list[1]
        gnt.broken_barh([(res_0, res_1 - res_0)], (1, 2),
                        facecolors=f'#{random.choice(randomhex)}'
                                   f'{random.choice(randomhex)}'
                                   f'{random.choice(randomhex)}'
                                   f'{random.choice(randomhex)}'
                                   f'{random.choice(randomhex)}'
                                   f'{random.choice(randomhex)}',
                        label=f'P{process.name}')
        if index % 3 == 0:
            value = -30
        elif index % 3 == 1:
            value = 0
        else:
            value = 30
        gnt.annotate(f'{process.termination_time}',
                     xy=(res_1, 2), xytext=(0, value),
                     xycoords='data',
                     textcoords='offset pixels', ha='center', va='center')

    # fix legend
    hand, labl = gnt.get_legend_handles_labels()
    handout = []
    lablout = []
    for h, l in zip(hand, labl):
        if l not in lablout:
            lablout.append(l)
            handout.append(h)
    gnt.legend(handout, lablout, prop={'size': 7-int(processes/20)},
               bbox_to_anchor=(1.07, 1))

    title = "CHART_FCFS_" + timestamp + ".png"
    sub = timestamp + "/"
    plt.savefig(sub + title)
