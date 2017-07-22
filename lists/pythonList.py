cars = ['bmw', 'toyota', 'jeep', 'cadillac', 'camry', 'nissan', 'honda']
cars.sort()
print (cars)

len(cars)
print(len(cars))
print(cars[3])
print (cars[-1])

for cars in cars:
    print (cars)

print(cars.title() +", amazing car!")

pizzas = ['cheese', 'ham', 'chicken', 'beef']
for pizza in pizzas:
    print (pizza)
    print(pizza.title() + ", wow delicious!!!, its yummy!!. \n")
print (pizza.title() +", wow delicious!!!, its yummy!!")

for value in range(1, 5):
    print (value)

numbers = list(range(1,6))
print (numbers)

even_numbers = list(range(2,11,2))
print (even_numbers)

odd_numbers = list(i for i in range(2, 11) if i%2!=0)
print(odd_numbers)

squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)

print(squares)

for value in range(1, 11):
    squares.append(value**2)
print (squares)

for value in range(10,20):
    print (value)
    squares.append(value**2)
    print (squares)




