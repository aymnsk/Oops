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
    
    def get_next_patient(self):
        if len(self.queue) == 0:
            print("The Queue is empty")
            return
        next_patient = self.queue.pop(0)
        print(f"{next_patient.name},Please go with the Dr")

    def remove_patient(self, name):
        patient_to_remove = [Patient for patient in self.queue if patient.name == name]
        for patient in patient_to_remove:
            self.queue.remove(patient)
        return len(patient_to_remove) > 0
    def print_patients(self):
        patients = [Patient for patient in self.queue]
        for patient in patients:
            print(f"Patient: {Patient.name} is {self.format_patient_status(patient.status)}")
    def is_full(self):
        return len(self.queue) >= self.MAX_CAPACITY
    def __str__(self):
        return f"{self.name}: There are {len(self.queue)} patients"

    @staticmethod
    def format_patient_status(status):
        if status == 0:
            return "Normal"
        elif status == 1:
            return "Urgent"
        return "Super-Urgent"
