# print ("Hello world")
# a = 100
# b = 200
# c = 300
# print(a, b, c, sep = '--', end = '#')

def helloWorld(a):
    a = a + 100
    b = a+11
    return a,b
a, _ = helloWorld(22)
print(a)