import random


def get_min_hash_functions():
    """
    Generates randomly pair of min hash functions of the form a*x + b
    :return An array containing pairs of form (a, b) for generating min hash functions
    """

    result = []
    for x in range(100):
        vector = []
        for y in range(2):
            vector.append(random.randint(1, 200))
        result.append(vector)
    
    return result


def find_sim_matrix(matrix):
    """
    Generates the similarity matrix of the documents based on the technique of min hashing
    :param matrix: Binary matrix (shingles * documents) which is formed after the shingling process
    :return Similarity matrix formed after applying min hashing technique
    """

    # We assume min hash functions to be of the form a*x + b modulo 200
    min_hash_functions = get_min_hash_functions()
    
    # Initialize similarity matrix elements to infinity
    similarity_matrix = []
    for x in range(100):
        vector = []
        for y in range(len(matrix[0])):
            vector.append(1000000)
        similarity_matrix.append(vector)


    # Update the similarity matrix for each hash function
    for x in range(len(matrix)):
        for y in range(100):
            hash_value = ((min_hash_functions[y][0]*(x+1)) + min_hash_functions[y][1])%50
            for z in range(len(matrix[0])):
                if matrix[x][z] == 1:
                    if hash_value < similarity_matrix[y][z]:
                        similarity_matrix[y][z] = hash_value 

    return similarity_matrix


if __name__ == "__main__":
    
    # Generate test matrix
    test_array = []
    for x in range(50):
        vector = []
        for y in range(5):
            vector.append(random.randint(0, 1))
        test_array.append(vector)

    similarity_matrix = find_sim_matrix(test_array)
    print(similarity_matrix)