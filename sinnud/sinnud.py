# first class for pip package test
# hope we can from FirstPipPackage import Sinnud
#
class Sinnud():
    def __init__(self, lastname="Du", firstname="Luke"):
        self.lname=lastname
        self.fname=firstname

    def printname(self):
        print(f"My name is {self.lname}, {self.fname}")