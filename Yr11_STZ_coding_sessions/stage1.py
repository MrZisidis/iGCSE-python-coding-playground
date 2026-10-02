# Import railway_data and display every service as one tidy line.
# Show the service code, the route, the departure time and the arrival time.
# Use a loop. Do not write ten print statements — that is not a program, that is typing.
# Line the columns up so it is readable.
# txt = f"We have {49:<8} chickens."
# print(txt)
# print(f"We have {49:<18} chickens.")

import railway_data as data

print("Service Code\tRoute\t\t\tDepartureTime\tArrivalTime")
print("*"*50)

for item in data.SERVICES:
    # print(item[0],"\t\t", item[3], item[4], item[2],"\t\t", item[1])
    txt = f"{item[0]:<12}\titem[3] item[4] item[2] item[1]"
    print(txt)


