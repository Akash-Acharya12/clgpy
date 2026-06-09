class complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag

    def add(self,other):
        real_part=self.real+other.real
