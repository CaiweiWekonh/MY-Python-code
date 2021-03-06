print("2021302191873,蔡威")
#Test 1
def boy_girl(filename):
    s1=c1=s2=c2=0
    with open (filename) as file1:
        file1txt=file1.read().split()
        for i in range(1,len(file1txt),4):
            s1+=int(file1txt[i])
            c1+=1
        for i in range(3,len(file1txt),4):
            s2+=int(file1txt[i])
            c2+=1
    print(c1,"boys\t",c2,"girls")
    print(s1,s2)
    print("Difference between boys and girls is",abs(s1-s2))
    print()

boy_girl("boy_girl.txt")

#Test 2
def even_num(filename):
    count=evencount=sum_all=0
    with open (filename) as file2:
        file2txt=file2.read().split()
        for number in file2txt:
            sum_all+=int(number)
            count+=1
            if int(number)%2==0:
                evencount+=1
    print(sum_all,"numbers,sum=",sum_all)
    print(evencount,"evens\t",evencount/count)
    print()

even_num("even_numbers.txt")

#Test 3
def negative_num(filename):
    with open (filename) as file3:
        file3txt=file3.read().split()
        sum_num=0
        count=0
        for num in file3txt:
            sum_num+=int(num)
            count+=1
            if sum_num<0:
                print("Sum of",sum_num,"after",count,"steps.")
                return True
    print("No negative sum.")
    return False

negative_num("negative_num1.txt")
negative_num("negative_num2.txt")
print()

#Test 4(ERROR)
def count_coins(filename):
    with open(filename) as file4:
        total=0
        file4txt=file4.read().split()
        for i in range(len(file4txt)):
            if file4txt[i].lower=="pennies":
                total+=int(file4txt[i-1])
            elif file4txt[i].lower=="nickels":
                total+=int(file4txt[i-1])*5
            elif file4txt[i].lower=="dimes":
                total+=int(file4txt[i-1])*10
            elif file4txt[i].lower=="quarters":
                total+=int(file4txt[i-1])*10
            else:
                continue
    print("Total Money:$",total/100)

count_coins("count_coins.txt")

#Test 5
def collapse_spaces(filename):
    with open (filename) as file5:
        file5txt=file5.read().split()
        print(file5txt[0],end="")
        for i in range(1,len(file5txt)):
            print("",file5txt[i],end="")

collapse_spaces("collapse_spaces.txt")
print()

#Test 6
def flip_line(filename):
    with open (filename) as file6:
        file6_flip=""
        for line in file6:
            file6_flip=line+file6_flip
    print(file6_flip)
    print()

flip_line("flip_line.txt")


#Test 7
def word_warp7(filename):
    with open (filename) as file7:
        linetxt=""
        for line in file7:
            for word in line:
                linetxt+=word
            if len(linetxt)<=60:
                print(linetxt)
            else:
                for i in range(len(linetxt)//60):
                    print(linetxt[int(60*i):int(60*i+60)])

word_warp7("flip_line.txt")
print()

#Test 8
def word_warp8(filename):
    with open (filename) as file7:

        linetxt=""
        linetxt_ss=""
        for line in file7:
            for word in line:
                linetxt+=word
            if len(linetxt)<=60:
                linetxt_s=linetxt
                linetxt_ss+=linetxt_s
            else:
                for i in range(len(linetxt)//60):
                    linetxt_s=linetxt[int(60*i):int(60*i+60)]
                    linetxt_ss+=linetxt_s
        print(linetxt_ss)
        
    with open (filename,"w")as file7:
        file7.write(linetxt_ss)

#word_warp8("flip_line.txt")

#Test 10
def coin_flip(filename):
    with open (filename) as file10:
        for line in file10.readlines():
            count=head=0
            for result in line:
                if result.lower()=='h':
                    head+=1
                    count+=1
                elif result.lower()=='t':
                    count+=1
                else:continue
            print("%dHeads(%f)."%(head,head/count))
            if head/count>0.5:
                print("You win!")
                print()

coin_flip("coin_flip.txt")
print()
                    
#Test12
def plus_scores(filename):
    with open (filename) as file12:
        i=1
        for line in file12.readlines():
            plus=count=0
            if i%2==1:
                print(line,end=":")
            else:
                for letter in line:
                     if letter=="+":
                        plus+=1
                        count+=1
                     elif letter=="-":
                         count+=1
                print("%f%%plus."%(100*plus/count))
            i+=1

plus_scores("plus_scores.txt")
print()

#Program 4
def write_a_story():
    filename=str(input("Input filename."))+".txt"
    adjective=str(input("Please enter an adjective."))
    pl_noun=str(input("Please enter a plural noun."))
    noun=str(input("Please enter a noun"))
    adjective2=str(input("Please enter an adjective."))
    place=str(input("Please enter a place"))
    with open (filename,"w") as file:
        file.write("One of the most %s characters in fiction is named \"Tarzan of %s\".\
Tarzan was raised by a/an %s and lives in the %s jungle in the heart of darkest %s."%(adjective,pl_noun,noun,adjective2,place))
    with open (filename,"r")as file:
        print(file.read())
write_a_story()    
    

                
            
