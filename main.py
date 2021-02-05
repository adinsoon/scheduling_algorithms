from process_plan import case_rr, case_fcfs
from page_swap import case_fifo, case_lru
import time
from utils import check_config
from config import config as cfg


timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")


if __name__ == '__main__':
    check_config(cfg)
    case_rr(timestamp)
    case_fcfs(timestamp)
    case_fifo(timestamp)
    case_lru(timestamp)
