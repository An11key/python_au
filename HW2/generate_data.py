import random

date = {
    'year': 2020,
    'month': 11
}
workers = ['_Ivanov_', '_Petrov_', '_Smirnov_', '_Eliseev_', '_Fadeev_']
place = 110
count = 10
data = ''
for i in range (30):
    new_str = '{},{},{},{}'.format('{}-{}'.format(date['year']+round(random.random()),('0'+str(1+round(date['month']*random.random())))[-2:]), place + round(10*random.random()), workers[round(random.random() * (len(workers)-1))], count+round(9*random.random()))
    # print(new_str)
    data += new_str + '\n'
data = data.strip()
print(data)
f = open('data.txt', 'w')
f.write(data)
f.close()

