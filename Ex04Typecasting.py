# typecasting : converting the data type of value to another type

x = 1
y = 2.0
z = '3'

x += int(z) # if u want to add x with z , z being string be temporatily casted to int.
print(x)
x = y
print(int(y))
print(x)
# convert int to float:
y= float(x)
print(y)