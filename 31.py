def sort_1(list):
    for i in range(0,len(list)-1):
        for q in range(i):
            if list[q] > list[q+1]:
                print("yo")
                list[q], list[q+1] = list[q+1], list[q]
    return list;

list = [1.3, 3.4, 3.9, 3.3, 2.8, 2.2, 3.7]
print (sort_1(list))