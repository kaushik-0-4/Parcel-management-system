from tkinter import *
from turtle import st
#from tkcalendar import Calendar
from LOGIN_BACKEND import INPUTS
from TRACKING_BACKEND import tracking
from tkinter import messagebox
from tkinter.ttk import Treeview
from tkinter import ttk
import tkinter as tk
from datetime import *
from write import store


#from write import store
import csv

def main():
    global a
    
    a=tracking()
    filename = "csv1.csv"
	
# writing to csv file
    with open(filename, 'r') as csv1: 
            items=csv.reader(csv1)
            for i in items:
                if i==[]:
                    continue
                else:
                    tracking_num=[]
                    for j in range(2,len(i)):
                        tracking_num.append(i[j])
                    a.pushSS([i[0],i[1]],tracking_num)
            a._iter_()
    
    

def submit():
        global track,details,z
        z=INPUTS()
        details = [e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get(),e11.get(),e12.get()]
        track = e10.get()

        z.push_(details)
        z.push(track)
        #_tracking()
def _tracking():
        global screen
        
        screen=LabelFrame(a,bd=2,relief="groove")
           
        screen.place(x=300,y=300,height=100,width=755)
        screen_label=Label(
            screen,
            text="Would you like to TRACK THE STATUS of your parcel ?",
            font="arial 16",
            bg="White",
            fg="black"
            ).grid(row=0,column=1)

        yes=Button(
            screen,
            text="YES",
            command = lambda : s2()
            ).grid(row=3,column=1)

        no=Button(
            screen,
            text="No",
            command= lambda : _back()).grid(row=3,column=3) 
      
        
def proceed():
    s=store()
    s.append_array()
    if e10.get()==ee1.get() and e9.get()==ee4.get() :
        print("*")
        main()
        track_num=[e10.get()]
        loc_pin=[e4.get(),e11.get()]
        #a.pushSS(loc_pin,track_num)

        p=a.getfront()
        status=0
    
        while a.getdest(p)[0]!=e9.get():
                p=a.getnext(p)
        p.t_s=True
        
        i=0
        while s.lst_p()[i][0]!=e9.get():
             i+=1
             
        if e10.get() not in s.lst_p()[i]:
                s.lst_p()[i].append(e10.get())
                p.t_n=s.lst_p()[i][2:len(s.lst_p()[i])]
                
                s=store(s.lst_p())
                s.append_array()
                status=1
        
        main()
        if status==1:
            for i in a.trackno(p):
                #print(i)
                pass
            messagebox.showinfo("STATUS OF THE PARCEL","PARCEL DELIVERED TO THE DESTINATION")
        else:
            print("Service not available")
            messagebox.showinfo("STATUS OF THE PARCEL","PARCEL IS YET TO BE  DELIVERED TO THE DESTINATION")
        print(a.getdest(p),a.trackno(p),a.track(p))
    else:
        no_track()
    #W.destroy()
def find():
    
        global Ln
        main()
        M= Tk()
        M.title("DATEWISE DELIVERIES")
        tv = Treeview(M,columns=(1,2), show='headings', height=8)
        tv.pack()
        find()
        tn=[Ln[0],Ln[1]]
            

        tv.heading(1, text="LOCATION")
        tv.heading(2, text="TRACKING NUMBER")
        for i in range(len(tn)):
            tv.insert(parent="",index=i,iid=i,values=(tn[i][0],tn[i][1]))
            style = Style()
            style.theme_use("default")
            style.map("Treeview")
        p=a.getfront()
        for i in range(a.getlen()):
            #print(a.getlen())
            if a.getdest(p)[1]==eee1.get():
                Ln=[a.getdest(p)[0],a.trackno(p)]

'


def FETCH_DETAILS():
    print("entereing")
    #z=INPUTS()
    for i in range(z.s1):
        print("details",i)
        if TRACKE.get()==z.b1[i]:
            print(z.a1[i])
        else:
            messagebox.showinfo("INVALID ENTRY","NO SUCH PARCELS IN THE TRACKING NUMBER")


    
def no_track():
        messagebox.showinfo(" TRACKING NUMBER NOT FOUND!!" ,"PLEASE CHECK THE TRACKING NUMBER")



def admin_login():
    global n,TRACK_NUM,TRACKE
    n=Tk()
    n.title("CUSTOMER DETAILS")
    TRACK_NUM=Label(n,text="TRACKING NUMBER").grid(row=0,column=0)
    TRACKE=Entry(n)
    TRACKE.grid(row=0,column=1)
    sub=Button(n,text="SEARCH",command=lambda : FETCH_DETAILS() )
    sub.grid(row=1,column=5)
def _back():
    screen.destroy()
    
def call_two():
    #submit()
    booking()
    submit()
        
def s1(p):
    global a,e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,z
    z=INPUTS()
    #global a,e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,z
    if p is not None:
        p.destroy()
    a1=Tk()
    a1.title("BOOKING PAGE")
    a1.geometry("1080x1000")
    l1=Label(a1,text="NAME OF THE CUSTOMER").grid(row=0,column=0)
    l2=Label(a1,text="PHONE NUM").grid(row=1,column=0)
    l3=Label(a1,text="ADDRESS").grid(row=2,column=0)
    l4=Label(a1,text="SOURCE").grid(row=3,column=0)
    l5=Label(a1,text="EMAIL").grid(row=4,column=0)
    l6=Label(a1,text="NAME OF THE CUSTOMER").grid(row=5,column=0)
    l7=Label(a1,text="PHONE NUM").grid(row=6,column=0)
    l8=Label(a1,text="ADDRESS").grid(row=7,column=0)
    l9=Label(a1,text="DESTINATION").grid(row=8,column=0)
    l10=Label(a1,text="TRACKING NUMBER").grid(row=9,column=0)
    l11=Label(a1,text="PINCODE OF THE SOURCE").grid(row=10,column=0)
    l12=Label(a1,text="PINCODE OF THE DESTINATION").grid(row=11,column=0)
    l13=Label(a1,text="EXPECTED DELIVERY DATE").grid(row=12,column=0)

    e1=Entry(a1)
    e2=Entry(a1)
    e3=Entry(a1)
    e4=Entry(a1)
    e5=Entry(a1)
    e6=Entry(a1)
    e7=Entry(a1)
    e8=Entry(a1)
    e9=Entry(a1)
    e10=Entry(a1)
    e11=Entry(a1)
    e12=Entry(a1)
    e13=Entry(a1)
    e1.grid(row=0,column=1)
    e2.grid(row=1,column=1)
    e3.grid(row=2,column=1)
    e4.grid(row=3,column=1)
    e5.grid(row=4,column=1)
    e6.grid(row=5,column=1)
    e7.grid(row=6,column=1)
    e8.grid(row=7,column=1)
    e9.grid(row=8,column=1)
    e10.grid(row=9,column=1)
    e11.grid(row=10,column=1)
    e12.grid(row=11,column=1)
    e13.grid(row=12,column=1)
    '''global cal
    cal=Calendar(a)
    cal.grid(row=18,column=1)'''
    sub=Button(a1,text="Submit",command=lambda : call_two() )
    sub.grid(row=20,column=5)
    subj=Button(a1,text="back",command=lambda : backs(a1) )
    subj.grid(row=20,column=7)
def backsS(ind):
    frontpage(ind)
    #ind.destroy()


    
def back(a):
    frontpage(a)

def s2():
    global ee1,e2,e3,ee4
    #main()
    '''if p is not None:
        p.destroy()'''
    a=Tk()
    a.title("TRACKING STATUS")
    a.geometry("1080x1000")
    l1=Label(a,text="ENTER THE TRACKING NUMBER").grid(row=12,column=0)
   
    l4=Label(a,text="ENTER THE LOCATION NAME OF THE DESTINATION ").grid(row=24,column=0)
    ee1=Entry(a)
    
    ee4=Entry(a)
    ee1.grid(row=12,column=1)
    
    ee4.grid(row=24,column=1)
    sub=Button(a,text="PROCEED",command=lambda : proceed() )
    sub.grid(row=50,column=5)


def s3(arrs):
    
    global eee1
    M=Tk()
    M.title("DATEWISE LIST OF DELIVERIES")
    global e1,e2,e3
    #a2.geometry("1080x1000")
    l1=Label(M,text="ENTER THE PINCODE").grid(row=0,column=0)
    eee1=Entry(M)
    eee1.grid(row=0,column=1) 
    sub=Button(M,text="SEARCH",command=lambda :find())
    sub.grid(row=50,column=5)
    r= Tk()
    r.title("PythonGuides")
    tv = ttk.Treeview(r,columns=(1,2), show='headings', height=8)
    tv.pack()
    guindy = Ln
    print("guindy",Ln)
    tv.heading(1, text="sender")
    tv.heading(2, text="Reciever")
    '''tv.heading(3, text="Date of depature")
    tv.heading(4,text="Tracking number")'''
    for i in range(len(guindy)):
        tv.insert(parent="",index=i,iid=i,values=(guindy[i][0],guindy[i][1]))
        style = ttk.Style()
        style.theme_use("default")
        style.map("Treeview")
    
    
    arrs.destroy()

def proceed1():
    c=0
    filename="csv1.csv"
    with open(filename, 'r') as csv1: 
            items=csv.reader(csv1)
            for i in items:
                #print("hii",i)
                if i==[]:
                    continue
                elif eeee4.get() in i:
                    c+=1
                    filename="csv1.csv"
                    with open(filename, 'r') as csv1: 
                        items=csv.reader(csv1)
                        for i in items:
                            #print("hii",i)
                            if i==[]:
                                continue
                            elif i[0]==eeee4.get():
                                if eeee1.get() in i:
                                    messagebox.showinfo("STATUS OF THE PARCEL","PARCEL DELIVERED TO THE DESTINATION")
                                else:
                                    messagebox.showinfo("STATUS OF THE PARCEL","NO SUCH PARCELS ")
    #w.destroy()
    if c==0:
        messagebox.showinfo("Destination","Destination Invalid")
    #w.destroy()

def status_tracking(windss):
    global eeee1,eeee4
    
    h=Tk()
    h.title("TRACKING STATUS")
    h.geometry("1080x1000")
    l1=Label(h,text="ENTER THE TRACKING NUMBER").grid(row=12,column=0)
   
    l4=Label(h,text="ENTER THE LOCATION NAME OF THE DESTINATION ").grid(row=24,column=0)
    eeee1=Entry(h)
    
    eeee4=Entry(h)
    eeee1.grid(row=12,column=1)

   
    
    eeee4.grid(row=24,column=1)
    sub=Button(h,text="PROCEED",command=lambda : proceed1() )
    sub.grid(row=50,column=5)
    sub=Button(h,text="BACK",command=lambda : backs(h) )
    sub.grid(row=50,column=4)
    windss.destroy()
    
def backs(wii):
    s7(wii)
    #wii.destroy()
def booking():
    s=store()
    s.append_array()

    i=0
    status=0
    
    while s.lst_p()[i][0]!=e9.get():
        i+=1
             
    if e10.get() not in s.lst_p()[i]:
            s.lst_p()[i].append(e10.get())
            #p.t_n=s.lst_p()[i][2:len(s.lst_p()[i])]
                
            s=store(s.lst_p())
            s.append_array()
            status=1

    main()
    
    p=a.getfront()
    while a.getdest(p)[0]!=e9.get():
        p=a.getnext(p)
    p.t_s=True

    messagebox.showinfo("BOOKING SUCCESFULL","ORDER PLACED ")

def s7(winds):
    g=Tk()
    g.title("CUSTOMER LOGIN MANAGEMENT SYSTEM")
    g.geometry("1080x1000")
    bb1=Button(g,text="STATUS TRACKING ",command=lambda:status_tracking(g)).grid(row=10,column=200)
    bb5=Button(g,text="PARCEL BOOKING ",command=lambda:s1(g)).grid(row=80,column=200)
    bb3=Button(g,text="UPDATES ",command=lambda:s3(g)).grid(row=60,column=200)
    bb4=Button(g,text="BACK ",command=lambda:backsS(g)).grid(row=90,column=200)
    winds.destroy()


def treeview():
    a2 = Tk()
    

    
def admin_password(window):
    def proceeding(windowS):
        if user.get()=="HK" and password.get()=="123":
            admin_login()
        else:
            messagebox.askretrycancel("Invalid Login","Invalid username or password")
        windowS.destroy()
    j=Tk()
    j.title("ADMIN DETAILS  MANAGEMENT SYSTEM")
    j.geometry("1080x1000")
    l1=Label(j,text="USERNAME").grid(row=0,column=0)
    l4=Label(j,text="PASSWORD ").grid(row=1,column=0)
    user=Entry(j)
    password=Entry(j)
    user.grid(row=0,column=1)
    password.grid(row=1,column=1)
    sub=Button(j,text="PROCEED",command=lambda:proceeding(j))
    sub.grid(row=50,column=5)
    window.destroy()
class password_cls:
    def __init__(self):
        self.s=0
        self.pass_dic={}
        self.push()
    def push(self):
        self.pass_dic["kaviya"]='hkservice'
        self.s+=1
        print(self.pass_dic)
    def find(self):
        print("<<<<<<<<<", self.username_login.get(), self.password_login.get())
        print(self.pass_dic.keys())
        if self.username_login.get() in self.pass_dic.keys():
            print(">>>>")
            if self.pass_dic[self.username_login.get()]== self.password_login.get():
                messagebox.showinfo("login","login successful")
                s7(h)
            elif self.pass_dic[ self.username_login.get()] !=  self.password_login.get():
                messagebox.showinfo("login","invalid password")
        else:
            messagebox.showinfo("login  failed","please check username or password")

    def password(self,winds):
        global user,passwords,h
        
        h=Tk()
        h.title("CUSTOMER LOGIN MANAGEMENT SYSTEM")
        h.geometry("500x300")
        h["bg"]="#a3f2f4"
        l0=Label(h,text="CUSTOMER LOGIN",font=("Helvetica",20),bg="#a3f2f4",fg="white",width=20,height=2).grid(row=0,column=0,pady=10)
        l1=Label(h,text="USERNAME",width=20,height=3,activebackground="blue",activeforeground="orange",bg="#8ce771",fg="white").grid(row=1,column=0,pady=10)
        l4=Label(h,text="PASSWORD ",width=20,height=3,activebackground="blue",activeforeground="orange",bg="#8ce771",fg="white").grid(row=2,column=0,pady=10)
        user=Entry(h)
        password=Entry(h)
        user.grid(row=1,column=1)
        password.grid(row=2,column=1)
        sub=Button(h,text="PROCEED",width=7,height=2,activebackground="blue",activeforeground="orange",bg="#8ce771",fg="white",command=lambda :s7(h) )
        sub.grid(row=3,column=1,pady=20)
        winds.destroy()

        #self.username_login = user.get()
        #self.password_login=passwords.get()


    #winds.destroy()'''
def frontpage(p=None):

    def log():
        s1(b)
    if p is not None:
        p.destroy()
    b=Tk()
    b.title("COURIER MANAGEMENT SYSTEM")
    b.geometry("1080x1000")
   
    def pincodes():
        s2()

    

        p.destroy()
    pasw=password_cls()
    w = Label(b, text='COURIER MANAGEMENT SYSTEM',font=("Arial",20),bg="black",fg="white",width=30,height=2).grid(row=1,column=20,pady=20,padx=40)
    b['bg']='#5ce2e4'
    bb2=Button(b,text="ADMIN ",width=20,height=3,activebackground="blue",activeforeground="orange",bg="black",fg="white",command=lambda:admin_password(b)).grid(row=2,column=20,padx=20)
    bb3=Button(b,text="CUSTOMER LOGIN ",width=20,height=3,activebackground="blue",activeforeground="orange",bg="black",fg="white",command=lambda:pasw.password(b)).grid(row=3,column=20,padx=20,pady=20)

frontpage(p=None)
mainloop()
'''bb2=Button(b,text="ADMIN ",command=lambda:admin_password(b)).grid(row=30,column=200)
    bb3=Button(b,text="CUSTOMER LOGIN ",command=lambda:pasw.password(b)).grid(row=50,column=200)

frontpage(p=None)
mainloop()'''
