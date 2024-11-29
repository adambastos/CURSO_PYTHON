weight = int(input("Weight: "))
opt = input("Kg or Lbs: ")

if opt == "k" or opt == "K":
    calckg = weight / 0.45
    print(str(calckg) + " Kg")
elif opt == "l" or opt == "L":
    calclbs = weight * 0.45
    print(str(calclbs) + " lbs")
else:
    print("Incorrect Answer!") 



 