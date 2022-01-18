one_marx = "Groucho"
print(one_marx)
print(type("Groucho",))
print(type(("Groucho",)))

marx_tuple = ('Groucho','chico','Harpo')

marx_tuple = ('Groucho','Chico','Harpo')
a , b , c = marx_tuple
print(a)

password = 'swordfish'
icecream = 'tuttirutti'
password, icecream = icecream ,password
print(password)

marx_list = ['Groucho','chico','Harpo']
print(tuple(marx_tuple))

a = (7,2)
b = (7,2,10,9)
print(a==b)

words = ('fresh','out','of','ideas')
for word in words:
    print(word)