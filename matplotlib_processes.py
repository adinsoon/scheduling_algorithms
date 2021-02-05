import matplotlib.pyplot as plt
from utils import roundup
import random
import math
from config import config as cfg
import os


dest = os.path.dirname(__file__)


def rr_plot(list_of_processes, timestamp):

    # every file will be saved to given dir
    target = dest + "/" + timestamp
    os.makedirs(target, exist_ok=True)
    os.path.join(target)

    # setting size of the plot according to the biggest termination time
    width_xaxis = []
    for process in list_of_processes:
        width_xaxis.append(process.termination_time)
    width_value = max(width_xaxis)
    height_value = cfg["RR"]["PROCESS_RANGE"] * 5 + 5

    # scalable plot
    WIDTH = math.ceil((width_value + 150) / 50)
    HEIGHT = math.ceil((height_value + 150) / 50)
    BAR_HEIGHT = 2

    fig, gnt = plt.subplots(figsize=(WIDTH, HEIGHT))

    plt.title(f'GANNT PLOT FOR {cfg["RR"]["PROCESS_RANGE"]} PROCESSES, RR, '
              f'QUANTUM {cfg["RR"]["QUANTUM"]} [MS]')

    # setting size of graph
    gnt.set_ylim(0, height_value)
    gnt.set_xlim(0, roundup(width_value + 15))

    gnt.set_xlabel('Time[ms]')
    gnt.set_ylabel('Process')

    gnt.set_yticks([i for i in range(5, cfg["RR"]["PROCESS_RANGE"] * 5 +
                                     5, 5)])
    gnt.invert_yaxis()

    # grid settings and visibility
    gnt.grid(True)
    gnt.set_axisbelow(True)

    names = []
    # mark results
    for index, process in enumerate(list_of_processes):
        names.append("P" + str(process.name))
        # show waiting times from lists
        for interval in process.waiting_list:
            gnt.broken_barh([(interval[0], interval[1] - interval[0])],
                            ((index * 5 + 5) - BAR_HEIGHT / 2,
                             BAR_HEIGHT),
                            facecolors='#8e8888', label='waiting time')
        # show working times from lists
        for interval in process.working_list:
            gnt.broken_barh([(interval[0], interval[1] - interval[0])],
                            ((index * 5 + 5) - BAR_HEIGHT / 2,
                             BAR_HEIGHT),
                            facecolors='#00ff00', label='burst time')
        # add termination time annotation to every process
        gnt.annotate(f'{process.termination_time}',
                     xy=(
                         process.termination_time,
                         index * 5 + 5 + BAR_HEIGHT / 2),
                     xytext=(BAR_HEIGHT * 10, 5),
                     xycoords='data',
                     textcoords='offset pixels', ha='center', va='center')

    gnt.set_yticklabels(names)

    # fix legend visibility
    hand, labl = gnt.get_legend_handles_labels()
    handout = []
    lablout = []
    for h, l in zip(hand, labl):
        if l not in lablout:
            lablout.append(l)
            handout.append(h)
    gnt.legend(handout, lablout, prop={'size': 6})

    # save to file
    title = "RR_CHART_" + timestamp + ".png"
    sub = timestamp + "/"
    plt.savefig(sub + title)


# used to generate random colors for fcfs plot
randomhex = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c',
             'd', 'e', 'f']


def fcfs_plot(list_of_processes, timestamp):

    # every file will be saved to given dir
    target = dest + "/" + timestamp
    os.makedirs(target, exist_ok=True)
    os.path.join(target)

    # setting size of the plot according to the biggest termination time
    width_xaxis = []
    for process in list_of_processes:
        width_xaxis.append(process.termination_time)
    width_value = max(width_xaxis)

    # resetting to default
    plt.style.use('default')

    # scalable plot
    WIDTH = math.ceil((width_value + 150) / 50)
    HEIGHT = math.ceil((len(list_of_processes)*16)/100)
    fig, gnt = plt.subplots(figsize=(WIDTH, max(HEIGHT, 4)))

    # title
    processes = cfg["FCFS"]["PROCESS_RANGE"]
    if cfg["SUB"]["USE_RR_TO_FCFS"]:
        processes = cfg["RR"]["PROCESS_RANGE"]
    plt.title(f'GANNT PLOT FOR {processes} PROCESSES, FCFS')

    # Y axis height
    gnt.set_ylim(0, 4)

    # X axis width according to the rounded biggest value of all termination
    # times
    gnt.set_xlim(0, roundup(width_value))

    # X, Y axis labels
    gnt.set_xlabel('Time[ms]')
    # I decided to left Y axis without label
    gnt.set_yticks([2])
    gnt.set_yticklabels([' '])

    gnt.invert_yaxis()

    # grid tools and visibility
    gnt.grid(True)
    gnt.set_axisbelow(True)

    # show working times of each process from the list
    for index, process in enumerate(list_of_processes):
        # working list consist of one sub-list
        res_0 = process.working_list[0]
        res_1 = process.working_list[1]
        gnt.broken_barh([(res_0, res_1 - res_0)], (1, 2),
                        # pick random color of process on graph
                        # disclaimer: sometimes it is difficult to read values
                        # on a blending-color background
                        facecolors=f'#{random.choice(randomhex)}'
                                   f'{random.choice(randomhex)}'
                                   f'{random.choice(randomhex)}'
                                   f'{random.choice(randomhex)}'
                                   f'{random.choice(randomhex)}'
                                   f'{random.choice(randomhex)}',
                        label=f'P{process.name}')
        # termination time annotation arrangement scheme
        if index % 3 == 0:
            # place lower (the lower value the lower placement)
            value = -30
        elif index % 3 == 1:
            # place even
            value = 0
        else:
            # place higher (the higher value the higher placement)
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

    # save to file
    title = "FCFS_CHART_" + timestamp + ".png"
    sub = timestamp + "/"
    plt.savefig(sub + title)
