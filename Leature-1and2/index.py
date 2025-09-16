x=1
y=2

y=x
x=y
print(x)
print(y)

#to swap use temp var and swap

b=":"
c=")"
s1=b+2*c #:))
print(s1)
f="a"
g=" b"
h="3"
# s2= (f+g)*(h) --> Type error
s2= (f+g)*int(h) #a ba ba b
print(s2)

s="ABC d3f ghi"
print(s)
print(s[3:len(s)-1]) # d3f gh
print(s[4:0:-1]) # d CB
print(s[6:3]) #will not give anything