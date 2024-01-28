#Q1
myfamily = ("mother", "father", "sister", "brother", "sister") 
print(myfamily)
print(type(myfamily)) #1
print(myfamily[2::2]) #2
Jay = list(myfamily) #3
Jay.append("me")
myfamily = tuple(Jay)
print(myfamily)
y = list(myfamily) #4
y.pop(3)
myfamily = tuple(y)
print(myfamily)