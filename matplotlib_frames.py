import matplotlib.pyplot as plt
from config import config as cfg


def frames_plot(mode, list_of_calls, list_of_frames, timestamp):

    if cfg["SUB"]["USE_FIFO_TO_LRU"]:
        mode = "FIFO"

    title_text = f'{mode} TABLE FOR {cfg[mode]["FRAMES_RANGE"]} FRAMES, ' \
                 f'{cfg[mode]["CALLS_RANGE"]} CALLS'

    WIDTH = cfg[mode]["CALLS_RANGE"]/6 + 4
    HEIGHT = cfg[mode]["FRAMES_RANGE"]/3
    fig, gnt = plt.subplots(figsize=(WIDTH, HEIGHT))
    adder = cfg[mode]["FRAMES_RANGE"]*cfg[mode]["CALLS_RANGE"]/100
    y_value = 0.85+adder
    plt.suptitle(title_text, y=min(y_value, 0.95), size=8)

    data = [list_of_calls]
    for frame in list_of_frames:
        data.append(frame.get_results())
    column_labels = [i for i in range(cfg[mode]["CALLS_RANGE"])]
    row_labels = ["CALLS"]
    for i in list_of_frames:
        row_labels.append(f'{str(i)}')

    gnt.axis('tight')
    gnt.axis('off')
    colColours = ["lime"] * cfg[mode]["CALLS_RANGE"]
    rowColours = ["gold"] + ["cornflowerblue"] * cfg[mode]["FRAMES_RANGE"]
    cellColours = []
    callColours = []

    for i in range(cfg[mode]["CALLS_RANGE"]):
        callColours.append("yellow")
    cellColours.append(callColours)
    for frame in list_of_frames:
        cell_row = []
        for item in range(cfg[mode]["CALLS_RANGE"]):
            if item in frame.log:
                cell_row.append("lightsalmon")
            else:
                cell_row.append("lightcyan")
        cellColours.append(cell_row)

    gnt.table(cellText=data, cellLoc='center', rowLabels=row_labels,
              colLabels=column_labels, cellColours=cellColours,
              rowLoc='center', loc='center', colColours=colColours,
              rowColours=rowColours)

    title = f"{mode}_TABLE_" + timestamp + ".png"
    sub = timestamp + "/"
    plt.savefig(sub + title)


