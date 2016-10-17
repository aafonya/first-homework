doors = []

for i in range(0,101):
     doors.append(False)

for j in range(1,101):
     for i in range(1,101):
         if i%j == 0:
             doors[i] = not doors[i]
            

      


print(doors)

for i in range(1,101):
    if doors[i] == True:
        print(i)


