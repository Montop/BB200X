DARPs = input("Are you using anti EpCAM DARPins? (y/n) ")
if DARPs == "y":
    epsilon = 15470
    molweight = 18000
else:
    epsilon = int(input("What is the extinction coefficient? "))
    molweight = float(input("What is the molecular weight? "))

amount = int(input("How many replicates? "))
replicates = []

for i in range(amount):
    replicates.append(float(input("Absorbance for replicate {}? ".format(i + 1))))

meanabs = sum(replicates) / len(replicates)

molconc = meanabs / epsilon

# 1 refers to the volume, it is assumed to be 1 L and will be converted to mL
# to give a concentration in mg mL⁻¹.
gramconc = molconc * 1 * molweight

print(str(molconc) + " M")
print(str(gramconc) + " mg mL⁻¹")
