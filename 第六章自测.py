print("蔡威",2021302191873)
print()
#Test 7
def main7():
    with open ("readme.txt")as file:
        count=0
        for s in file:
            print("Input:",s)
            count+=1
        print(count,"total")

main7()
print()

#Test 8
def main8():
    with open ("readme.txt")as file:
        count=0
        for s in file.read().split():
            print("Input:",s)
            count+=1
        print(count,"total")

main8()
