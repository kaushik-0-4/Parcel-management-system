import ctypes
class INPUTS:
    def __init__(self):
        self.c=20
        self.a1=(ctypes.py_object*self.c)()
        self.b1=(ctypes.py_object*self.c)()
        self.s1=0
        self.s2=0
    
    def push_(self,e):
        
        if (self.s1 == self.c):
            self._resize(2 * self.c)
        self.a1[self.s1]= e
        self.s1 += 1
        print(self.a1[:self.s1])
    
    def push(self,e):
        if (self.s2 == self.c):
            self.resize(2 * self.c)
        self.b1[self.s2] = e
        self.s2 += 1
        print(self.b1[:self.s2])
    def _resize(self, cap: int):
        
        temp =(ctypes.py_object*cap)()
        for index in range(self.s1):
            temp[index] = self.a1[index]
        self.a1 = temp
        self.c= cap
    def resize(self, cap: int):
        
        temp =(ctypes.py_object*cap)()
        for index in range(self.s2):
            temp[index] = self.a1[index]
        self.b1 = temp
        self.c= cap
    

    def display(self,tn):
        for i in range(self.s2):
            if self.b1[i]==tn:
                print(self.a1[i])
            else:
                pass
    def show(self):
        return self.a1,self.b1
    #def check(self):

    
