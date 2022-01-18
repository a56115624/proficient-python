""" print(another_empty_list)

a = list('cat')
print(a)

a_tuple = ('ready','fire','aim') 
print(list(a_tuple))

talk_like_a_pirate_day = '9/19/2019'
print(talk_like_a_pirate_day.split('/'))

splitme = 'a/b//c/d///e'
print(splitme.split('/'))

splitme = 'a/b//c/d///e'
print(splitme.split('//'))

marxes = ['Groexho','chico','Harpo']
print(marxes[0])
print(marxes[-1])

marxes = ['Groucho','chico','Harpo']
print(marxes[0:2])
print(marxes[::2])
print(marxes[::-2])

marxes = ['Groucho','Chico','Harpo']
marxes.append('Zeppo')
print(marxes)

marxes = ['Groucho','Chico','Harpo']
marxes.insert(2,'Gummo')
print(marxes)

a = ['blath']*3
print(a)

marxes = ['Groucho','Chico','Harpo','Zeppo']
others = ['Gummo','Karl']
marxes.extend(others)

marxes = ['Groucho','Chico','Harpo','Zeppo']
others = ['Gummo','Karl']
marxes = marxes+others
print(marxes)

marxes = ['Groucho','Chico','Harpo','Zeppo']
others = ['Gummo','Karl']
marxes.append(others)
print(marxes)
= ['Groucho','Chico','Harpo']
marxes[2]='Wanda'
print(marxes)

numbers = [1,2,3,4]
numbers[1:3]=[8,9]
print(numbers)

numbers = [1,2,3,4]
numbers[1:3]='wat?'
print(numbers)

marxes = ['Groucho','Chico','Harpo','Gummo','Karl']
del marxes[-1]
print(marxes)

marxes = ['Groucho','Chico','Harpo','Gummo','Karl']
marxes.remove('Groucho')
print(marxes)

marxes = ['Groucho','Chico','Harpo','Gummo','Karl']
marxes.clear()
print(marxes)

marxes = ['Groucho','Chico','Harpo','Gummo','Karl']
print(marxes.index('Harpo'))

marxes = ['Groucho','Chico','Harpo','Gummo','Karl']
print("Gummo" in marxes)

marxes = ['Groucho','Chico','Harpo','Gummo','Karl']
print(marxes.count('Chico'))

marxes = ['Groucho','Chico','Harpo']
','.join(marxes)
print(marxes)

numbers = [2,1,4.0,3]
numbers.sort()
print(numbers)

numbers = [2,1,4.0,3]
numbers.sort(reverse=True)
print(numbers)

marxes = ['Groucho','Chico','Harpo']
print(len(marxes))




a = [1,2,3]
b = a
a[0]='surprise'
print(b)

a = [1,2,[8,9]]
b = a.copy()
c = list(a)
d = a[:]
print(d)

a = [1,2,[8,9]]
a[2][1]=10
b = a.copy()
c = list(a)
d = a[:]
print(d)
 """
""" # cheeses = ['brie','gjetost','havarti']
# for cheese in cheeses:
#     print (cheese)

cheeses = ['brie','gjetost','havarti']
for cheese in cheeses:
    if cheese.startswith('g'):
        print("I want eat anything that starts with 'g'")
        break
    else:
        print(cheese) """

""" cheeses = ['brie','gjtost','havarti']
for cheese in cheeses:
    if cheese.startswith('x'):
        print("I wont eat anything that starts with 'x'")
        break
    else:
        print(cheese)
else:
    print("Didnt find anything that started with 'x'") """

""" 
cheeses = []
for cheese in cheeses:
    print("This shop has some love , cheese")
    break
else:
    print("This is not much of a cheese shop, is it") """

""" 
days = ['Monday','Tuesday','Wednesday']
fruits = ['banana','orange','peach']
drinks = ['coffee','tes','beer']
desserts = ['tiramisu','ice cream','pie','pudding']

for day,fruit,drink,dessert in zip (days,fruits, drinks,desserts):
    print(day, ":drink",drink,"-eat",fruit, "-enjoy",desserts)
 """
""" english = 'Monday','Tuesday','Wednesday'
french = 'Lundi','Mardi','Mercredi'
print(list(zip(english,french)))
print(dict(zip(english,french))) """

""" number_list = []
number_list.append(1)
number_list.append(2)
number_list.append(3)
number_list.append(4)
number_list.append(5)
print(number_list)
 """
""" number_list = []
for number in range(1,6):
    number_list.append(number)

print(number_list) """

""" number_list = list(range(1,6))
print(number_list) """

""" number_list = [number for number in range(1,6)]
print(number_list) """

""" number_list = [number-1 for number in range(1,6)]
print(number_list) """


""" a_list = [number for number in range(1,6) if number % 2 == 1]
print(a_list)

a_list = []
for number in range(1,6):
    if number % 2 == 1:
        a_list.append(number)

print(a_list)
 """

""" rows = range(1,4)
cols = range(1,3)
for row in rows:
    for col in cols:
        print(row,col) """
""" 
rows = range(1,4)
cols = range(1,3)
cells = [(row,col)for row in rows for col in cols]
for cell in cells :
    print(cell) """

