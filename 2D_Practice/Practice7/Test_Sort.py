data = [23, 22, 19, 1, 100, 10000, 40, 56700, 20000]

def bubble_sort(data):
    for i in range(0, len(data)):
        for j in range(i+1, len(data)):
            if data[i] < data[j]:
                data[i], data[j] = data[j], data[i]

bubble_sort(data)
print(data)