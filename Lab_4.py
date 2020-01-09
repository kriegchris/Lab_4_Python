import sys

def squared(n):
    myList = []
    
    for number in range(1, n+1):
        myList.append(number**2)
    
    return myList

def cubed(n):
    myList = []
    
    for number in range(1, n+1):
        myList.append(number**3)
        
    return myList

def main(args):
    print("Learn your squares and cubes!")
    cont = "y"
    while (cont == "y"):
        num = input("Enter an integer: ")
        num = int(num)
        print('{:<10s}{:>4s}{:>12s}'.format("Number", "Squared", "Cubed"))
        print('{:<10s}{:>4s}{:>12s}'.format("======", "=======", "====="))
        squared_list = squared(num)
        cubed_list = cubed(num)
        for nums in range(0, len(squared_list)):
            print('{:<10d}{:>4d}{:>12d}'.format(nums+1, squared_list[nums], cubed_list[nums]))
        cont = input("Continue? (y/n): ")
    

if __name__ == '__main__':
    
    sys.exit(main(sys.argv))
