a=input("Name of the student:")
b=int(input("Age:"))
c=input("passout date(dd mm yyyy):").split('-')
d=float(input("CGPA:"))
e=input("College Name:")
f=input("Stream:")
g=list(input("Programming Languages:").split())
h=tuple(input("Languages:").split())
i=eval(input("Subject(input as set format):"))
j=set(input("Project Details:").split())
k=bool(input("Any Backlogs:"))

print("Hello",a,"\t your age is",b)
print("your  passed out date is",c,end='\n',)
print( "you have got",d,"CGPA")
print("your college is:",e,end="\n")
print("your stream is",f)
print(f"programming languages: {g} \n | Languages: {h} \n| subject: {i}")
print("project details:",j)
print("Any Backlogs:",k)


