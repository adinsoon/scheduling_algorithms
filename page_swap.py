from fifo import fifo_algorithm as fifo
from generators import generate_calls, generate_frames
from matplotlib_frames import frames_plot
from utils import save_calls, save_pages
from config import config as cfg


list_of_calls: list = []
list_of_frames: list = []


def case_fifo(timestamp):
    # generate list of calls and pages
    global list_of_calls, list_of_frames
    list_of_calls = generate_calls(cfg["FIFO"]["CALLS_RANGE"],
                                   cfg["FIFO"]["CALLS_VALUE_RANGE"])
    list_of_frames = generate_frames(cfg['FIFO']['FRAMES_RANGE'])
    reason = 'FIFO_CALLS'
    if cfg["SUB"]["USE_FIFO_TO_LRU"]:
        reason = "FIFO_&_LRU_CALLS"
    # save generated calls
    save_calls(reason, list_of_frames, timestamp)

    # execute the algorithm
    fifo_result = fifo(list_of_calls, list_of_frames)

    # save results
    save_pages('FIFO_DONE', list_of_calls, fifo_result, timestamp)

    # # make a plot
    # frames_plot()


def case_lru():
    pass
