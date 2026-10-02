# Import railway_data and display every service as one tidy line.
# Show the service code, the route, the departure time and the arrival time.
# Use a loop. Do not write ten print statements — that is not a program, that is typing.
# Line the columns up so it is readable.
# txt = f"We have {49:<8} chickens."
# print(txt)
# print(f"We have {49:<18} chickens.")

import railway_data as data

title = "Service Code\tRoute\t\t\t\tDepartureTime\tArrivalTime"
print(title)
print("*"*(len(title)+15))

for item in data.SERVICES:
    # print(item[0],"\t\t", item[3], item[4], item[2],"\t\t", item[1])
    txt = f"{item[0]:<12}\t{item[3]}-{item[4]}\t{item[1]:<15}\t{item[2]}"
    print(txt)


