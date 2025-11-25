import time
import numpy as np

size_array= 10000
a = np.random.randint(0, 10000, size_array)


print(f'### start sorting {size_array} elements')
start_time_full = time.time()

start_time = 0
for i in range(0, int(len(a)/2)):
    if i == 0:
        start_time = time.time()

    maximum = minimum = a[i]
    index_min = index_max = 0
    swap_min = swap_max = False
    size = len(a)-i
    for j in range(i, size):
        if a[j] <= minimum:
            minimum = a[j]
            index_min = j
            swap_min = True
        if a[j] >= maximum:
            maximum = a[j]
            index_max = j
            swap_max = True

    if swap_min:
        a[index_min], a[i] = a[i], a[index_min]
        # in case the maximum is the same as the element moved above, the index should be changed
        if maximum == a[index_min]:
            index_max = index_min

    if swap_max:
        a[index_max], a[size-1] = a[size-1], a[index_max]

    #if (i != 0) & (i % 1000 == 0):
        #print('cycle: ', i)

        #end_time = time.time()
        #time_lapsed = end_time - start_time
        #print(time_lapsed)


        start_time = time.time()

end_time_full = time.time()
time_elapsed_full = end_time_full - start_time_full
print('time elapsed algorithm: ', time_elapsed_full)
print('### finishing sorting:')

flag = True
i = 1
while i < len(a):
    if a[i - 1] > a[i]:
        flag = False
        break
    i += 1

# printing result
if flag:
    print("TRUE, Array is sorted.")
else:
    print("FALSE, Array is not sorted.")

#print(a)