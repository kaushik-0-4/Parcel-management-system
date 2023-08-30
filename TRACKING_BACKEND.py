class node:
    def __init__(self,pincode=[],t_s=False,t_n='',next=None,pre=None):
        self.pincode=pincode
        self.t_s=t_s
        self.t_n=t_n
        self.pre=pre
        self.next=next
class tracking:
    def __init__(self):
        self.head=node()
        self.head.next=self.head
        self.head.pre=self.head
        self.tail=self.head
        self.size=0
    def pushSS(self,l1,l2):
        if self.size==0:
            self.head.pincode=l1
            self.head.t_n=l2
            self.size+=1
        else:
            new=node(pincode=l1,t_n=l2,next=self.tail.next,pre=self.tail)
            self.tail.next=new
            self.tail=new
            self.size+=1
    def _iter_(self):
        c=0
        p=self.tail.next
        while c!=self.size:
            ele=p.pincode
            element=p.t_n
            print(ele)
            print( element)
            p=p.next
            c+=1
    def check(self,input,destination):
        p=self.head
        status=0
        for i in range(self.size):
            if p.pincode[0]==destination:
                p.t_s=True
                p.t_n.append(input)
                status=1
            else:
                p=p.next
        if status==1:
            for i in p.t_n:
                print(i)
        else:
            print("Service not available")
        print(p.pincode,p.t_s,p.t_n)
    
    def track(self,m,l):
        p=self.head
        while p.pincode[0]!=l:
            
            p=p.next
        p.t_s=True
        print(p.t_s)
    

    def getlen(self):
        return self.size

    def getfront(self):
        return self.head

    def getnext(self,p):
        return p.next
    
    def getdest(self,p):
        return p.pincode
    
    def track (self,p):
        return p.t_s
    
    def trackno(self,p):
        return p.t_n



            
'''t=tracking()
.pushSS(['trichy',630006],[20221234])
#print("ITER")

t.pushSS(['chennai',630008],[20221235])
t.pushSS(['madurai',630004],[20224567])
t.pushSS(['karaikudi',630003],[2022459])
t._iter_()
t.check(20221235,'trichy','chennai')
t.check(20221234,'trichy','karaikudi')
t.check(20220000,'chennai','karaikudi')
t.track(20221234,'karaikudi'
#print(t.getfront())
print(t.getdest(t.getfront()))'''