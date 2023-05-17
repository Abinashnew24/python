'''
a=4
ch='a'
name='sabin'

print (a)
print (ch)
print (name)
 
print (type(a),type(ch), type(name))

# Area of triangle 

a = int(input('enter the 1st number: '))
b = int (input('enter the 2nd number: '))

sum=a+b
print ('the sum is',sum ) 

print (2*3)
print (2**3)
a=int(input('enter 1st side: '))
b=int(input('enter 2st side: '))
c=int(input('enter 3st side: '))

s= (a+b+c)/2

A= (s*(s-a)*(s-b)*(s-c))**1/2

print ('area is',A)
#for loop

name = 'Lumbini'
for i in name:
    print (i)
    
    for i in range (2,4):
        print (i)
        
# if_else 
num = int (input('enter the 1st number: '))

if num==0:
    print ('number is neither even nor odd',num)
elif num%2==0: 
    print ('number is even')  
else: 
    print ('number is odd')   
#Tuple 
t = (1,'a','string',1+8)
print (t)
print(type(t))
print(t[2])    

tup = t+(4,5,6)
print (tup)

i = list (tup)
print (i)
print(type(i))

#Dictionary 

dict = {
    1:'sabin',
    2:'csit',
    3:'8th'
}
print(dict)
print(type(dict))

dict[4]='something'
print(dict)

#break #continue

for i in range (1,10):
    if (i==4):
        break;
    print(i)
    
for i in range (1,10):
    if (i==4):
        continue;
    print(i) '''
    
#function    
'''
def sum(a,b,c):
    print('sum',a+b+c)
sum(2,3,4)   
 
def checker(a,b): 
    if a>b: 
        print ("{0} is greater than {1}".format(a,b))
    elif b>a:
        print ("{0} is greater than {1}".format(b,a)) 
    else:
        print('a and b are equal')
checker(5,5) '''

# Calculator
'''
class Calculator:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        return a/b
    
    def fi(self,a,b):
        return a/b
    def module(self,a,b):
        return a%b
    
obj = Calculator()
print ("Addition is {0}".format(obj.add(2,3)))
print ('Subtraction is {0}'.format(obj.sub(6,7)))
print ('multiplication is {0}'.format(obj.mul(4,4)))
print ('division is {0}'.format(obj.div(3,4)))    
    '''
#inheritance
''''
class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname+ ' ' +self.lastname)
x=person('sabin','adhikari')
x.printname()

class student(person):
    def first(self):
        print('i am student')

y=student('abinash','poudel')
y.printname()
y.first()                    '''

'''''
class vechical:
    def vechical(self):
        print("wheel")  

class bike(vechical):
    def bike (self):
        print('hello ns')
class ns(bike):
    def ns(self):
        print('ns 200')
obj = ns()
obj.ns()
obj.vechical()
obj.bike()                          
       
class bird:
    def fly(self):
        print('can fly')
class parrot(bird):
    def speak(self):
        print('can talk')
class eagle(bird):
    def flyhigh(self):
        print('can fly high')
class penguin(bird):
    def walk(self):
        print('can walk') 
obj=penguin()
obj.walk()
obj.fly()
obj.speak()

obj=eagle()
obj.flyhigh()    '''

'''''
class bird:
    def fly(self):
        print('can fly')
class parrot():
    def speak(self):
        print('can talk')

class penguin(bird,parrot):
    def walk(self):
        print('can walk') 
obj=penguin()
obj.walk()
obj.fly()
obj.speak()
'''
#pyramid
''''
def pyramid(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print('* ',end=" ")
        print ('\r')
pyramid(5)           
'''
'''''
class rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
        
    
    def area(self):
        a=self.length*self.width
        print('area of rectangleis: ',a)
    
    def perimeter(self):
        p=2*(self.length+self.width) 
        print('perimeter of rectangle is:',p)
obj=rectangle(5,6)
obj.area()
obj.perimeter()           
'''
'''''
class Bank:
    def __init__(self,balance,account):
        self.balance=balance
        self.account=account
    
    def Deposit(self,money):
        self.balance += money    
        print("Total balance: ",self.balance)
        
    def withdraw(self,money):
        self.balance  -= money
        print('total balance:',self.balance) 
obj=Bank(10000,26273)
obj.Deposit(2000) 
obj.withdraw(1000)        
'''
'''''
from multipledispatch import dispatch
@dispatch(int,int)
def Product(a,b):
    print(a*b)
@dispatch(int,int,int)
def Product(a,b,c):
    print(a*b*c)
@dispatch(float,float,float)    
def Product(a,b,c):
    print(a*b*c)
Product(2,3)
Product(2,3,4)
Product(2.1,2.3,2.4)
  '''
'''
def pyramid(n):
    num=1 
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(num,end=" ")
            num=num+1
        print ('\r')
pyramid(5)             
'''
fruits=['apple','banana','avogado','orange','alu']
newlist=[]
for i in fruits:
    if len(i)>3 and i[0]=='a':
        newlist.append()
newlist.reverse()
print(newlist)        
        
    