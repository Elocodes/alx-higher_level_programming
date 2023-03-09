#!/usr/bin/python3

my_list = ['01', '02', '03', '04', '05', '06', '07', '08', '09']

for each_digit in range(10, 90):
    num = str(each_digit).split()
    (a, b) = num.pop()
    a + b == b + a
    my_list.append(a + b)
    #if a + b in my_list:
        #my_list.pop()
    #a + b == b + a
    #if a + b in my_list:
        #my_list.pop(b + a)
    #if a != b:
        #my_list.append(a + b)
        #a + b == b + a
       # if 
        #if b + a == (a + b in my_list):
           # break;
    #if (a != b) and ((a + b) != (b + a)): # or ((a != b) and (b + a not in my_list)):
        #cast2int = int(a + b)
        #my_list.append(cast2int)
print(f"{my_list}", end='')
