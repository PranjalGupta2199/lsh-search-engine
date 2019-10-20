import os
from hashlib import sha256 as sha


shingle_size = 9


def create_shingle():
    '''
    Creates shingles of size k from documents in
    the corpus
    :returns shingle set and hashed shingle set
    '''
    shingle_set = set()
    shingle_set_hashed = set()
    dir = os.listdir("../corpus")
    dir.sort()
    for file in dir:
        with open(os.path.join("../corpus", file), 'r') as file_obj:
            data = file_obj.read()
            for i in range(0, len(data) - shingle_size + 1):
                shingle = data[i:i + shingle_size]
                shingle_set.add(shingle)
                hash_value = int(sha(shingle.encode('utf-8')
                                     ).hexdigest(), 16) % 10 ** 4
                shingle_set_hashed.add(hash_value)

    return shingle_set, shingle_set_hashed


def create_shingle_matrix(shingle_set):
    '''
    Creates boolean vector shingle matrix.
    :returns 2D array
    '''
    matrix_list = []
    dir = os.listdir("../corpus")
    dir.sort()
    for file in dir:
        with open(os.path.join("../corpus", file), 'r') as file_obj:
            temp_list = []
            data = str(file_obj.read())
            for shingle in shingle_set:
                if data.find(shingle) == -1:
                    temp_list.append(0)
                else:
                    temp_list.append(1)
            matrix_list.append(temp_list)

    return list(map(list,zip(*matrix_list)))


def print_shingle_matrix(matrix_list):
    for array in matrix_list:
        print(array)


if __name__ == "__main__":
    shingle_set, shingle_set_hashed = create_shingle()
    shingle_matrix = create_shingle_matrix(shingle_set)
    print_shingle_matrix(shingle_matrix)