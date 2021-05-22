import matplotlib.pyplot as plt

workers = ['_Ivanov_', '_Petrov_', '_Smirnov_', '_Eliseev_', '_Fadeev_']
resources = [i + 110 for i in range(10)]


def Refactor():
    f = open('data.txt', 'r')
    data = []
    for line in f:
        line_data = line.strip().split(',')
        dict_data = {
            'date': line_data[0],
            'resource': line_data[1],
            'staff_id': line_data[2],
            'count': line_data[3]
        }
        data.append(dict_data)
    return data



def filter_count(min_date, max_date, source, source_data, data):
    count = 0
    for item in (filter(lambda res: (res[source]) == str(source_data) and max_date > res['date'] > min_date, data)):
        count += int(item['count'])
    return count


def build():
    data = Refactor()
    min_date = '2020-01'
    max_date = '2022-06'
    plt.figure()
    plt.subplot(1,2,1)
    CountByResource = []
    for i in range(len(resources)):
        CountByResource.append(filter_count(min_date, max_date, 'resource', resources[i], data))
    plt.xlabel('Resources')
    plt.ylabel('Count')
    plt.title('From {} to {}'.format(min_date,max_date))
    plt.bar(resources, CountByResource)

    plt.subplot(1, 2, 2)
    CountById = []
    for i in range(len(workers)):
        print(workers[i])
        CountById.append(filter_count('2010-01', '2022-01', 'staff_id', workers[i], data))
    plt.xlabel('Id')
    plt.ylabel('Count')
    plt.title('From {} to {}'.format(min_date, max_date))
    plt.bar(workers, CountById)

    plt.show()


build()
