from fifo import fifo_algorithm as fifo
from lru import lru_algorithm as lru
from generators import generate_calls, generate_frames
from matplotlib_frames import frames_plot
from utils import save_calls, save_pages
from config import config as cfg
from copy import deepcopy


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
    if cfg["EXE"]["TXT"]:
        save_calls(reason, list_of_calls, timestamp)

    # execute the algorithm
    fifo_result = fifo(list_of_calls, list_of_frames)

    # save results
    if cfg["EXE"]["TXT"]:
        save_pages('FIFO_DONE', list_of_calls, fifo_result, timestamp)

    # make a plot
    if cfg["EXE"]["GRAPHS"]:
        frames_plot('FIFO', list_of_calls, fifo_result, timestamp)


def case_lru(timestamp):
    if not cfg["SUB"]["USE_FIFO_TO_LRU"]:
        # generate list of calls and frames
        list_of_calls_lru = generate_calls(cfg["LRU"]["CALLS_RANGE"],
                                           cfg["LRU"]["CALLS_VALUE_RANGE"])
        list_of_frames_lru = generate_frames(cfg['LRU']['FRAMES_RANGE'])
        reason = 'LRU_CALLS'
        # save generated calls
        if cfg["EXE"]["TXT"]:
            save_calls(reason, list_of_calls_lru, timestamp)
    else:
        # copy previous generated
        list_of_calls_lru = deepcopy(list_of_calls)
        list_of_frames_lru = deepcopy(list_of_frames)

    # execute the algorithm
    lru_results = lru(list_of_calls_lru, list_of_frames_lru)

    # save results
    if cfg["EXE"]["TXT"]:
        save_pages('LRU_DONE', list_of_calls_lru, lru_results, timestamp)

    # make a plot
    if cfg["EXE"]["GRAPHS"]:
        frames_plot('LRU', list_of_calls_lru, lru_results, timestamp)
