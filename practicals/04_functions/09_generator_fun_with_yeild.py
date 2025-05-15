# Q: Write a generator function that yields even numbers up to a specific limit.

limit = int(input("Enter the limit of this range: "))

def even_generator(limit):
    for i in range(2, limit+1, 2):
        yield i

for num in even_generator(limit):
    print(num)
