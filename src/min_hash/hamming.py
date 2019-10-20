import random

def find_signature_matrix(shingle_matrix, number=100):
    '''
    Generates signature matrix for Hamming Family
    by choosing random rows.
    '''
    dimension = len(shingle_matrix)

    signature_matrix = [shingle_matrix[random.randint(0, dimension)]
                        for it in range(number)]

    return signature_matrix