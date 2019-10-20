import min_hash
import k_shingles
import lsh
import os


def main():
    shingle_set, shingle_set_hashed = k_shingles.create_shingle()
    shingle_matrix = k_shingles.create_shingle_matrix(shingle_set)
    print (len(shingle_matrix[0]))
    signature_matrix = min_hash.find_sim_matrix(shingle_matrix)

    search_result = lsh.locality_sensitive_hashing(signature_matrix)

    dir = os.listdir("../corpus")
    dir.sort()
    sample_doc_index = dir.index('sample.md')


    for bands in search_result.keys():
        for hash_val, doc_list in search_result.items():
            print (hash_val , ": ", doc_list)
        print()


    '''
    for bucket in search_result:
        for band, index_list in search_result[bucket]:
            if (sample_doc_index in index_list):
                print (band)
    '''

if __name__ == "__main__":
    main()