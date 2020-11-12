c1 = float(input("What is the initial concentration? (M) "))
c2 = float(input("What is the target concentration? (M) "))
V2 = float(input("What is the target volume? (L) "))

V1 = (c2 * V2) / c1

print("{:e}".format(V1) + " L")
