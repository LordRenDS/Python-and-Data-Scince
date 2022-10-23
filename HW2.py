import numpy as np


# Write a function basic_stats(np_array), where np_array has 2
# dimensions. Find the basic statistics of a given flattened array.
def basic_stats(np_arr):
    print('Original array: \n' + str(np_arr))
    print('Flattened array: ' + str(np_arr.flatten()))
    print('It consists of ' + str(np_arr.size) + ' values')
    print('Number of dimensions: ' + str(np_arr.ndim))
    print('Number of elements in the each dimension: ' + str(np_arr.shape))
    print('Maximum value: ' + str(np_arr.max()))
    print('Minimum value: ' + str(np_arr.min()))
    rows = np_arr.ndim - 1
    colum = np_arr.ndim - 2
    print('Minimum values per rows: ' + str(np_arr.min(axis=rows)))
    print('Maximum values per rows: ' + str(np_arr.max(axis=rows)))
    print('Minimum values per columns: ' + str(np_arr.min(axis=colum)))
    print('Maximum values per columns: ' + str(np_arr.max(axis=colum)))
    print('Summation value: ' + str(np_arr.sum()))
    print('Average value: ' + str(np_arr.mean()))
    print('*-' * 25 + '*')


a = np.asarray([[1, 2, 3], [4, 5, 6]])
b = np.array([[1, 5, 9], [14, 19, 27], [38, 45, 59]])
c = np.array([[1, 2, 3], [4, 5, 6], [14, 19, 27], [38, 45, 59], [99, 123, 111], [345, 567, 899]])

basic_stats(a)
basic_stats(b)
basic_stats(c)
print('-' * 50)

# Create a numpy array that consists of random numbers. In for cycle
# increment every element and update it in the existent array. Convert
# dtype of the array into int64. astype(np.int64)
a = np.random.randint(20, size=9)
print('Input array: ' + str(a))
dx = 0
for i in a:
    i *= 2
    a[dx] = i
    dx += 1
a = a.astype(np.int64)
print('Dtype: ' + str(a.dtype))
print('Output array with cycle: ' + str(a))

# Solve the 2nd task above using broadcasting instead of for loop.
broadcasting = a * 2
print('Output array with broadcasting: ' + str(broadcasting))
print('-' * 50)


# Create a function iter_matrix_mul(arr_a, arr_b) that gets 2 parameters: 2
# matrices as numpy arrays. Using a for loop, transpose the 1st matrix.
# Then check the dimensions of matrices. If it is possible to multiply them,
# do it using a for loop. (You will need to create a result matrix that is full of
# zeros and fill it with numbers as you proceed with calculations in a for
# loop). If it’s not possible to multiply them, return an empty numpy array.
def iter_matrix_mul(arr_a, arr_b):
    if arr_a.ndim == 2 and arr_b.ndim == 2:
        # transport
        x = arr_a.shape
        transport_arr = np.zeros((x[1], x[0]), dtype=np.int64)
        raw = 0
        colum = 0
        for j in arr_a:
            for i in j:
                transport_arr[colum][raw] = arr_a[raw][colum]
                colum += 1
            raw += 1
            colum = 0
        # multiple
        if len(transport_arr[0]) == len(arr_b):
            raw = 0
            colum = 0
            raw_t = 0
            colum_t = 0
            result = np.zeros((len(transport_arr), len(arr_b[0])), dtype=np.int64)
            for j in result:
                for i in j:
                    mul = transport_arr[raw_t] * arr_b[0:len(arr_b), colum_t]
                    result[raw][colum] = mul.sum()
                    colum += 1
                    colum_t += 1
                raw += 1
                colum = 0
                raw_t += 1
                colum_t = 0
            print(result)
        else:
            print(np.array([]))
    else:
        print('Is\'t a 2D matrix')


A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[1, 2], [3, 4]])
iter_matrix_mul(A, B)
A = np.array([[1, 2], [4, 5], [6, 7]])
B = np.array([[1, 2], [3, 4]])
iter_matrix_mul(A, B)


# Solve the 4th task using built-in NumPy methods without a for loop.
# Name the function numpy_matrix_mul(arr_a, arr_b)
def numpy_matrix_mul(arr_a, arr_b):
    if arr_a.ndim == 2 and arr_b.ndim == 2:
        arr_a = arr_a.T
        if len(arr_a[0]) == len(arr_b):
            result = np.matmul(arr_a, arr_b)
            print(result)
        else:
            print(np.array([]))
    else:
        print('Is\'t a 2D matrix')


A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[1, 2], [3, 4]])
numpy_matrix_mul(A, B)
A = np.array([[1, 2], [4, 5], [6, 7]])
B = np.array([[1, 2], [3, 4]])
numpy_matrix_mul(A, B)
print('-' * 50)
