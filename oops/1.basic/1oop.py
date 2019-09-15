class Computer:

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("configuration is: ", self.cpu, self.ram)


com1 = Computer("i5","4gb")

print("using Computer.config(com1):------------------")
Computer.config(com1)

print("using com1.config():---------------------------")
com1.config()