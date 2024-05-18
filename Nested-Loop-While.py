count = 1
x= 0
y=0

while (x<5):
    x= x+1
    count = count*3
    y=0
    while (y<10):
        y=y+1
        count =count+3
        if count <1000:
            print(count)
print ("Count is Bigger than 1000")