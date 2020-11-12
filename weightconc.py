c = float(input("What is the target concentration? (M) "))
MW = float(input("What is the molecular weight? "))
V = float(input("What is the target volume? (L) "))

m = c * MW * V

print("{:e}".format(m) + " g")
