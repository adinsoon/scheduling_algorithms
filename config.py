# config file for algorithms
config = {
    "SUB": {
        # use same params for RR and FCFS
        "USE_RR_TO_FCFS": 1,
        # use same params for FIFO and LRU
        "USE_FIFO_TO_LRU": 1,
    },
    # ROUND-ROBIN
    "RR": {
        # how many processes to generate
        "PROCESS_RANGE": 35,
        # specify the range of arrivals
        "ARRIVAL_RANGE": 5,
        # specify the range of durations (>0)
        "DURATION_RANGE": 25,
        # appends to the given list
        "QUANTUM": 5,
    },
    # FCFS
    "FCFS": {
        # how many processes to generate
        "PROCESS_RANGE": 15,
        # specify the range of arrivals
        "ARRIVAL_RANGE": 5,
        # specify the range of durations (>0)
        "DURATION_RANGE": 25,
    },
    # FIFO
    "FIFO": {
        # how many calls to generate
        "CALLS_RANGE": 15,
        # specify the range of calls value
        "CALLS_VALUE_RANGE": 5,
        # how many frames to generate
        "FRAMES_RANGE": 8,
    },
    # LRU
    "LRU": {
        # how many calls to generate
        "CALLS_RANGE": 15,
        # specify the range of calls value
        "CALLS_VALUE_RANGE": 5,
        # how many frames to generate
        "FRAMES_RANGE": 8,
    },
}
