import math

def main():
    AB=float(input("Enter the length of AB : "))
    AC=float(input("Enter the length of AC : "))
    BC=math.sqrt(AB**2+AC**2)
    print("The length of BC (the hypotenuse) is :  " ,str(BC))

if __name__ == "__main__":
    main()
