scores = []
total = 0
end = False
while end == False:
    scores.append(int(input("Enter a score (0-100):")))
    if scores == -1:
        end = True
    for score in scores:
        total = total + score
    print("Total is: " + str(total))