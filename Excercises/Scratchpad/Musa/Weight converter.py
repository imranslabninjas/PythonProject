weight=int(input("Weight:"))
unit=input("(K)g or (L)bs:")
if unit=="L" or "l":
    converted = weight*2.205
    print("Weight in Lbs:"+str(converted))
elif unit=="K" or "k":
    converted = weight*0.45
    print("Weight in Kgs:"+str(converted))