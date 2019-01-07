from multiprocessing import Queue
from multiprocessing import Process

class CSVGenerator:
    def __init__(self):
        self.queu = Queue()
        self.stopRequests = Queue()

    def run(self):
        while self.stopRequests.empty():
            work_on = self.queu.get(timeout=3)

