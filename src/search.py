from min_hash import jaccard, cosine, hamming
import k_shingles
import lsh
import os


def main():
    #query = input("Enter your query: ")
    #print ()

    #with open('../corpus/sample.md', 'w') as f:
    #    f.write(query)

    shingle_set, shingle_set_hashed = k_shingles.create_shingle()
    shingle_matrix = k_shingles.create_shingle_matrix(shingle_set)
    signature_matrix = hamming.find_signature_matrix(shingle_matrix)

    search_result = lsh.locality_sensitive_hashing(signature_matrix)

    dir = os.listdir("../corpus")
    dir.sort()
    sample_doc_index = dir.index('sample.md')
    #print(sample_doc_index)

    for band_num in search_result:
        print (band_num, )
        for hash_val, docs in search_result[band_num].items():
            print (hash_val, docs)
        print ()

if __name__ == "__main__":
    main()