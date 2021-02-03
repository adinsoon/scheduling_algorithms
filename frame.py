
class Frame:

    logs_FIFO: dict = {}
    logs_LRU: dict = {}

    def __init__(self, name):
        # FID
        self.name = name
        # reload time
        self.reload: int = 0
        # present value
        self.value: int = 0
        # dict of previous values
        self.values: dict = {}
        self.taken: bool = False

    def __str__(self):
        return f'F{self.name}'

    def get_results(self):
        return list(self.values.values())

    @classmethod
    # for FIFO
    def get_percent_hit_fifo(cls):
        hits = sum(occur == "HIT" for occur in Frame.logs_FIFO.values())
        return round(hits / len(Frame.logs_FIFO), 3)

    @classmethod
    # for FIFO
    def get_percent_fault_fifo(cls):
        faults = sum(occur == "FAULT" for occur in Frame.logs_FIFO.values())
        return round(faults / len(Frame.logs_FIFO), 3)

    @classmethod
    # for LRU
    def get_percent_hit_lru(cls):
        hits = sum(occur == "HIT" for occur in Frame.logs_LRU.values())
        return round(hits / len(Frame.logs_LRU), 3)

    @classmethod
    # for LRU
    def get_percent_fault_lru(cls):
        faults = sum(occur == "FAULT" for occur in Frame.logs_LRU.values())
        return round(faults / len(Frame.logs_LRU), 3)
