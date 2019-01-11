# from https://gist.github.com/Renien/9672f174e31b6f96f356da09eb481d2c

import numpy as np

def jaccard_similarity_score(x, y):
    intersection_cardinality = len(set(x).intersection(set(y)))
    union_cardinality = len(set(x).union(set(y)))
    return intersection_cardinality / float(union_cardinality)

if __name__ == "__main__":
    score = jaccard_similarity_score(np.array([0, 1, 2, 5, 6]), np.array([0, 2, 3, 5, 7, 9]))
    print ("Jaccard Similarity Score : ", score)
