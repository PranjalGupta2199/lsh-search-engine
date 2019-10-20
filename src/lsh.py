import zlib
import itertools


band = 4

def locality_sensitive_hashing(signature_matrix):
    band_size = int(len(signature_matrix)/band)
    doc_size = len(signature_matrix[0])
    bucket = {}
    bucket_size = 100

    if (len(signature_matrix)%band != 0):
        band_size += 1

    for var in range(0,band):
        temp_bucket = {}
        for doc_id in range(doc_size):
            try:
                hash_vector = [signature_matrix[row][doc_id]
                    for row in range(var*band_size,(var+1)*band_size)]
            except IndexError:
                hash_vector = [signature_matrix[row][doc_id]
                    for row in range(var*band_size,len(signature_matrix))]

            hash_val = zlib.crc32(bytes(hash_vector)) % bucket_size

            if (temp_bucket.get(hash_val) == None):
                temp_bucket[hash_val] = set()

            temp_bucket[hash_val].add(doc_id)
        bucket[band] = temp_bucket

    return bucket


            

if __name__ == "__main__":
    v = [[i,i+1,i+2] for i in range (1,21,3)]
    print (locality_sensitive_hashing(v))