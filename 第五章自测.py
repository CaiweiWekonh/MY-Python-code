print("蔡威2021302191873")
#第五章自测题
#自测1
def main1a():
    x=1
    while x<100:
        print(x,end=" ")
        x+=10
        print() #执行9次
        
main1a()

def main1b():
    max=10
    while max<10:
        print("count down:",max)
    max-=1

main1b() #执行0次

def main1c():
    x=250
    while x%3!=0:
        print(x)#执行无数次

def main1d():
    x=2
    while x<200:
        print(x,end=" ")
        x*=x
    print()

main1d()#执行3次

def main1e():
    word="a"
    while len(word)<10:
        word="b"+word+"b"
        print(word)#执行5次
    print()

main1e()

def main1f():
    x=100
    while x>0:
        print(x//10)
        x=x//2#执行7次
    print()

main1f()

#自测2
'''a.n=1
  while n<=max:
      print(n)
      n+=1
b.total=25
  number=1
  while number<=total//5+1:
      total-=number
      print(total,number)
      number+=1
c.i=1
  while i<3:
      j=1
      while j<4:
          k=1
          while k<5:
              print("*",end=" ")
              k+=1
        print("!",end=" ")
        j+=1
    i+=1'''

#自测3
def main3(x):
    y=1
    z=0
    while 2*y<=x:
        y=y*2
        z+=1
    print(y,z)

main3(1)
main3(6)
main3(19)
main3(39)
main3(74)

#自测4
def main4(x):
    y=0
    while x%2==0:
        y+=1
        x=x//2
    print(x,y)

main4(19)
main4(42)
main4(48)
main4(40)
main4(64)
print()

#自测5
def main5():
    import random
    x=0
    x=random.randint(0,10)
    print(x)
    print()

main5()

#自测6
def main6():
    import random
    x=0
    x=random.randrange(55,99,2)
    print(x)
    print()
    
main6()    
    
#自测7
def print_letters(text):
    for i in range(len(text)-1):
        print(text[i]+"-",end="")
    print(text[-1])
    print()

print_letters("mother")
print_letters("c")

#自测8
def main8():
    x=int(input("Type a number(-1 to quiut)."))
    max=min=x
    while x!=-1:
        if max<x:
            max=x
        elif min>x:
            min=x
        x=int(input("Type a number(-1 to quiut)."))
        if x==-1:
            print("maxmum=",max)
            print("minimum=",min)
  
main8()

#自测9
def main9():
    x=27
    y=-1
    z=32
    b=False
    print(not b)
    print(b or True)
    print((x>y)and (y>z))
    print((x==y)or (x<=z))
    print(not(x%2==0))
    print(b and not b)
    print(b or not b)
    print((x<y)==b)
    print(not (x/2==13)or b or (z*3==96))
    print((z<x)==False)
    print(not (x>0)and (y<0))
    print()

main9()

#自测10
def is_vowel(s):
    for ss in "aeiouAEIOU":
        if s==ss:
            return True
    return False

def main10():
    s=str(input("Type a char."))
    if is_vowel(s):
        print(s,"is an vowel!")
    else:
        print(s,"is not a vowel!")

main10()

#自测11
def is_prime(n):
    prime=True
    for i in range(2,n):
        if n%i==0:
            prime=False
    return prime
print(is_prime(1))
print(is_prime(2))
print(is_prime(9))
print()

#自测12
def start_end_same(string):
    return string[0]==string[-1]

print(start_end_same("start"))
print(start_end_same("wow"))
print()

#自测13
def has_pennies(cents):
    return cents%5==0

#自测14
def main14(x,y):
    while x!=0 and y!=0:
        if x<y:
            y-=x
        else:
            x-=y
    return x+y

print(main14(3,3))
print(main14(5,3))
print(main14(2,6))
print(main14(12,18))
print(main14(30,75))
print()

#自测15
'''days=get_total_since_1980()
years=1980
while days>365:
    if is leap_year(year):
        if days>366:
            day-=366
            year+=1
        else:
            days-=365
            year+=1
    else:
        if days>365:
            days-=365
            years+=1
        else:
            days-=364
            years+=1'''

#自测16
def main16():
    x=27
    y=-1
    z=32
    b=False
    print(True)
    print((x<=y)or(y<=z))
    print((x!=y)and(x>=z))
    print((x%2!=0)or b)
    print((x/2!=13)and b and(z*3==96))
    print((z>=x) or (z<=y and x<y))
    print()

main16()

#自测17(错误）
def main17():
    age_s=input("Your age?")
    gpa_s=input("Your gpa?")
    while not(is_float(gpa_s)and is_int(age_s))or not 0.0<=float(gpa_s)<=4.0:
        print("Type again.")
        age_s=input("Your age?")
        gpa_s=input("Your gpa?")
    age=int(age_s)
    gpa=float(gpa_s)
    print("Age is",age)
    print("Gpa is",gpa)
    print()

def is_int(i):
    try:
        i=int(i)
        return True
    except ValueError:
        return False
        
def is_float(f):
    try:
        f=float(f)
        return True
    except ValueError:
        return False
    

main17()

#自测18
def main18():
    x=input("The first number?")
    y=input("The second number?")
    z=input("The third number?")
    while not (is_int(x)and is_int(y)and is_int(z)):
        print("Type again(integer).")
        x=input("The first number?")
        y=input("The second number?")
        z=input("The third number?")
    s=int(x+y+z)
    print("The average is",s/3)
    print()

main18()

#自测19
def mystery(x):
    y= int(input("Type a number: "))
    count=0
    #Point A(SOMETIMES SOMETIMES NEVER)
    while y < x:
        #Point B(ALWAYS SOMETIMES NEVER)
        if y==0:
            count+=1
            #Point C(ALWAYS ALWAYS ALWAYS)
        y=int(input("Type a number:"))
        # Point D(SOMETIMES SOMETIMES SOMETIMES)
    # Point E(NEVER SOMETIMES SOMETIMES)
    return count

#自测20
def main20(n):
    a=random.randint(1,3)
    b=2
    #Point A(SOMETIMES SOMETIMES SOMETIMES)
    while n>b:
        #Point B(ALWAYS SOMETIMES SOMETIMES)
        b+=a
        if a>1:
            n-=1
            #Point C(SOMETIMMES ALWAYS ALWAYS)
            a=random.randint(1,b)
        else:
            a=b+1
            #Point D(NEVER ALWAYS NEVER)
    #PointE
    return n

#自测21
def main21():
    prev=0
    count=0
    nexts=int(input("Type a number"))
    #Point A(SOMETIMES ALWAYS SOMETIMES)
    while nexts!=0:
        #Point B(NEVER ALWAYS NEVER)
        if nexts==pev:
            #Point C(NEVER NEVER ALWAYS)
            count+=1
        prev=nexts
        nexts=int(input("Type a number."))
        #Point D(SOMETIMES NEVER SOMETIMES)
    #Point E(ALWAYS ALWAYS ALWAYS)
    return count

    
            

    
    
     
        
