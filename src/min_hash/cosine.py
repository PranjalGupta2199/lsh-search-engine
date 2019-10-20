import random


def get_normal_vectors(number, dimensions):
    '''
    Generate 'n' normal vectors for hyperplanes
    '''

    comp = [1,-1]
    norm_vector_list = []

    for it in range (number):
        rand_vector = [random.choice(comp) \
            for d in range (len(dimensions))]
        norm_vector_list.append(rand_vector)

    return norm_vector_list


def dot_product(vector_A, vector_B):
    '''
    Calculates the dot product of 2 vectors A and B and
    returns 1 if value is positive and 0 otherwises
    '''
    val = 0

    for comp1, comp2 in zip(vector_A, vector_B):
        val += comp1*comp2

    return val > 0


def find_signature_matrix(shingle_matrix, number=100):
    '''
    Generates signature matrix for Cosine Family 
    using random normal vectors.
    '''

    doc_len = len(shingle_matrix[0])
    dimension = len(shingle_matrix)
    norm_vectors = get_normal_vectors(number, dimension)


    signature_matrix = []

    for doc_id in range(doc_len):
        hash_vector = [shingle_matrix [var][doc_id]
                       for var in range(dimension)]

        for index,vec in enumerate(norm_vectors):
            hash_value = dot_product(hash_vector, vec)
            signature_matrix[index][doc_id] = hash_value

    return signature_matrix


