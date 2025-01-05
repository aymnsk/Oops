from patient import *

class Specialization:
    MAX_CAPACITY = 10
    PATIENT_STATUS_NUMBER = [0,1,2]

    def __init__(self,name):
        self.name = 'Specializtaion' + name
        self.queue = []

    def add_pat(self,name,status):
        if len(self.queue) >= self.MAX_CAPACITY:
            print("Apologies, the queue in this specialization.")
            return
        if status not in self.PATIENT_STATUS_NUMBER:
            print("Invalid status. Status should be 0 (normal), 1 (urgent), or 2 (super-urgent).")
            return
        new_pat = Patient(name, status)
        self.queue.append(new_pat)
        self.queue.sort(key=lambda x: x.status, reverse=True)
        print(f"Patient: {new_pat.name} is {self.format_patient_status(new_pat.status)}")
    