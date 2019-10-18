import zlib
import itertools


band_size = 4

def locality_sensitive_hashing(sim_matrix):
    band_row_size = int(len(sim_matrix)/band_size)
    doc_size = len(sim_matrix[0])
    bucket = {}
    bucket_size = 100

    if (len(sim_matrix)%band_size != 0):
        band_row_size += 1

    for band in range(0,band_size):
        for doc_id in range(doc_size):
            try:
                hash_vector = [sim_matrix[row][doc_id]
                    for row in range(band*band_row_size, \
                        (band+1)*band_row_size)]
            except IndexError:
                hash_vector = hash_vector = [sim_matrix[row][doc_id] \
                    for row in range(band*band_row_size,len(sim_matrix))]

            hash_val = zlib.crc32(bytes(hash_vector)) % bucket_size

            if (bucket.get(hash_val) == None):
                bucket[hash_val] = set()
                bucket[hash_val].add(doc_id)
            else:
                bucket[hash_val].add(doc_id)

    return bucket


            

if __name__ == "__main__":
    v = [[i,i+1,i+2] for i in range (1,21,3)]
    print (locality_sensitive_hashing(v))