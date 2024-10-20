#1.
#def add(a:int,b:int)-> int:
#    return a + b
#a = int(input())
#b = int(input())
#print("a+b={}",format(add(a+b)))
#2.
#N = int(input(""))
#if N >=0 and N % 10 != 0:
#    a = str(N)[::-1]
#    print(a)
#elif N < 0 and N % 10 != 0:
#    b = -N
#    c = str(b)[::-1]
#    i = -int(c)
#    print(i)
#elif N >= 0 and N % 10 == 0:
#    d = N // 10
#    f = str(d)[::-1]
#    print(f)
#elif N < 0 and N % 10 == 0:
#    g = N // 10
#    h = str(-g)[::-1]
#    j = -int(h)
#    print(j)
#3.
str = (input(""))
num_0 = 0
num_1 = 0
num_2 = 0
num_3 = 0
num_4 = 0
num_5 = 0
num_6 = 0
num_7 = 0
num_8 = 0
num_9 = 0
for i in str:
    if i == '0':
        num_0 += 1
    elif i == '1':
        num_1 += 1
    elif i == '2':
        num_2 += 1
    elif i == '3':
        num_3 += 1
    elif i == '4':
        num_4 += 1
    elif i == '5':
        num_5 += 1
    elif i == '6':
        num_6 += 1
    elif i == '7':
        num_7 += 1
    elif i == '8':
        num_8 += 1
    elif i == '9':
        num_9 += 1
print(f'num_0: {num_0}\nnum_1: {num_1}\nnum_2: {num_2}\nnum_3: {num_3}\nnum_4: {num_4}\nnum_5: {num_5}\nnum_6: {num_6}\nnum_7: {num_7}\nnum_8: {num_8}\nnum_9: {num_9}')