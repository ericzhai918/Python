def avg(list):
    return sum(list) / len(list)


def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)

print(drop_first_last((99,99,88,33,2,99,11)))


record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
print(name)
print(phone_numbers)

*trailing,current = [10, 8, 7, 1, 9, 5, 10, 3]
print(trailing)
print(current)
