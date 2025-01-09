import cv2
import numpy as np
import random

coverage = 10
size = 128

def populateObstacles(image):

    currentCoverage = 0

    # Scan the array as long as the desired coverage has not been met
    while currentCoverage < coverage:

        # Pick a random point in the array
        # Bounds are in place to ensure that Tetrominos are not placed outside of the array
        m = random.randint(0, image.shape[0] - 3)
        n = random.randint(1, image.shape[0] - 2)

        if image[m, n] == 1:
            # Pick random number based on the desired coverage
            # Should help with distributing the Tetrominos more
            check = random.randint(0, 100)
            if check < coverage:
                # Select which Tetromino to place based on a random number
                blockNumber = random.randint(1, 4)

                # I Tetromino
                if blockNumber == 1:
                    image[m, n] = 0
                    image[m-1, n] = 0
                    image[m-2, n] = 0
                    image[m-3, n] = 0

                # L Tetromino
                if blockNumber == 2:
                    image[m, n] = 0
                    image[m - 1, n] = 0
                    image[m - 2, n] = 0
                    image[m - 2, n+1] = 0

                # S Tetromino
                if blockNumber == 3:
                    image[m, n] = 0
                    image[m - 1, n] = 0
                    image[m - 1, n+1] = 0
                    image[m - 2, n+1] = 0

                # T Tetromino
                if blockNumber == 4:
                    image[m, n] = 0
                    image[m-1, n] = 0
                    image[m-1, n-1] = 0
                    image[m-2, n] = 0

        # Calculate current coverage
        nonzero = np.count_nonzero(image)
        temp = (nonzero/(size**2)) * 100
        currentCoverage = 100 - temp

    return image

if __name__ == "__main__":
    # Create a blank/white array/image
    image = np.ones((size, size))

    # Generate obstacles
    image = populateObstacles(image)

    # Display the array/image
    # cv2.imwrite("Obstacle_Field_10.png", image*255)
    cv2.imshow("Obstacle Field", image)
    cv2.waitKey(0)

