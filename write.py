import csv
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


from ArrayList import ArrayList

class store():
    def __init__(self,lst=[]):
        if lst ==  []:
            self.lst=[['MADURAI',625001],['Chennai',600007],['Trichy',620001],['ramanathapuram',623524],['karaikudi',620003],['srirangam',6200006],['coimbatore',641006],['namakkal',637001],['erode',638001],['salem',636001],['virudhunagar',626001],['kanyakumari',623153]]
        else:
            self.lst=lst
        #self.append_array()
    def num(self):
        return len(self.lst)

    def lst_p(self):
        return self.lst

    def append_array(self):
        global a
        a=ArrayList()
        for i in range(len(self.lst)):
            a.insert(i,self.lst[i])
        self.write()
        print(a.__str__())


    def write(self):
        filename = "csv1.csv"	
    # writing to csv file
        with open(filename, 'w') as csv1:
            csvwriter=csv.writer(csv1)
            for item in range(a.end()):
                csvwriter.writerow(a.__getitem__(item))
            


s=store()
s.append_array()      
