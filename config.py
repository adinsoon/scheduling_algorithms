# config file for algorithms
config = {
    "SUB": {
        # use same params for RR and FCFS
        "USE_RR_TO_FCFS": 1,
        # "USE_FIFO_TO_LRU": 0,
    },
    # ROUND-ROBIN
    "RR": {
        # how many processes to generate
        "RR_PROCESS_RANGE": 35,
        # specify the range of arrivals
        "RR_ARRIVAL_RANGE": 5,
        # specify the range of durations (>0)
        "RR_DURATION_RANGE": 25,
        # appends to the given list
        "RR_QUANTUM": 5,
    },
    # FCFS
    "FCFS": {
        # how many processes to generate
        "FCFS_PROCESS_RANGE": 5,
        # specify the range of arrivals
        "FCFS_ARRIVAL_RANGE": 5,
        # specify the range of durations (>0)
        "FCFS_DURATION_RANGE": 25,
    },
}

