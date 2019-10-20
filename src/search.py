from min_hash import jaccard, cosine, hamming
import k_shingles
import lsh
import os


def find_similar_docs(bucket, doc_id):
    '''
    Find similar docs for the given doc_id
    :param 
        bucket dict Contaning bands and the corresponding
            docs with similar hash value
        doc_id int Document id of the query
    :return
        Set containing similar docs
    '''
    doc_result = []

    for band in bucket :
        for hash_val, docs in bucket[band].items():
            if doc_id in docs:
                doc_result += docs

    doc_result.sort()
    return list(set(doc_result))


def process_query(query, lsh_family_measure):
    '''
    Prints docs similar to query by using the lsh_family_measure
    :param
        query string
        lsh_family_measure <function>
    :return
        void
    '''

    shingle_set, shingle_set_hashed = k_shingles.create_shingle()
    shingle_matrix = k_shingles.create_shingle_matrix(shingle_set)
    signature_matrix = lsh_family_measure.find_signature_matrix(shingle_matrix)

    search_result = lsh.locality_sensitive_hashing(signature_matrix)

    dir = os.listdir("../corpus")
    dir.sort()
    sample_doc_index = dir.index('sample.md')
    
    print("Your query is in doc : ",sample_doc_index)

    for band_num in search_result:
        print (band_num, )
        for hash_val, docs in search_result[band_num].items():
            print (hash_val, docs)
        print ()

    similar_docs = find_similar_docs(search_result, sample_doc_index)
    print ("Similar docs are : ",)
    for doc_id in similar_docs: 
        print(dir[doc_id], end=',')
    print ()



def main():
    query = input("Enter your query: ")
    print ()

    with open('../corpus/sample.md', 'w') as f:
       f.write(query)


    print("Waiting for Search Results ....")
    print ("With Jaccard measure : ")
    process_query(query, jaccard)
    print ("With cosine measure : ")
    process_query(query, cosine)
    print ("With hamming measure : ")
    process_query(query, hamming)


if __name__ == "__main__":
    main()