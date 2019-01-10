import sys
import numpy as np
import jaccard
import segmentation
import request

def download_filed(path):
    return 0

if __name__ == '__main__':
    if (len(sys.argv) == 1):
        path = "path/to/files"
        request.download_filed(path)
    else:
        path = sys.argv[1]

    # Compute each segmentation on each image stored in path
    # contours[0] : expected data
    # contours[0] : watershed result
    # contours[0] : level sets result
    contours = segmentation.all(path)

    print("# Compute Jaccard score for each image")
    # Display the jaccard mean score between the expected data and the segmentation result
    for i in range(1, len(contours)):
        print(" -- " + segmentation.labels[i] + " -- ")
        sum = 0
        for j in range(len(contours[0])):
            score = jaccard.jaccard_similarity_score(contours[i][j], contours[0][j])
            sum += score
            print(score)
        mean = sum / len(contours[0])
        print("mean : " + str(mean))
