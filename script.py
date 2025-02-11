#Enter distance prompt
distance = float(input("Enter the distance :"))
#Enter time prompt

time = float(input("Enter the time :"))
#Calculate distance by using Speed / Time

#Zero distance handler
if distance == 0:
    print("Cannot calculate speed when distance is zero.")

#Zero time handler
elif time == 0:
    print("Cannot calculate speed when time is zero.")
#Speed calculation
else:
    speed = distance / time
    print(f"The speed is {speed:.2f} M/S")