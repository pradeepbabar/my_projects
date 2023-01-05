#level 4  exercise

#4.1
from crete_python_module import avg
num_list = []

with open('level4', 'r') as f:
    for line in f:
        num_list.append(float(line.rstrip('\n')))

print(num_list)
print(avg(num_list))

#4.2

city = []

with open('city', 'r') as c:
    for line in c:
        city.append(line.rstrip('\n'))

    print('Before sorting', city)

    y = sorted(city)
    print('After Sort', y)

#executing ooutput in new file
with open('orderd_city_list.txt', 'w') as w:
    for c in city:
        w.write(c + '\n')
print('done')