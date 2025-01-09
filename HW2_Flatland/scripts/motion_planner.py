import random
import numpy as np
import matplotlib.pyplot as plt

from gridworld import populateObstacles

size = 128
coverage = 10
counter_max = 200000

start_location_x = 1
start_location_y = 1

end_location_x = 100
end_location_y = 100

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

def dfs(modImage):

    # Create queue list
    queue = []

    # Create binary matrix to check if location has been checked
    checked = np.zeros((size, size))

    # Create pointers to track location
    x_pointer = start_location_x
    y_pointer = start_location_y

    # Mark start position as checked
    checked[y_pointer, x_pointer] = 1

    # Determine connecting nodes from initial location
    # Load (append) them into the queue in order of R, D, L, U
    # Save as tuples of type (x, y), then store in list

    # Up
    if all(modImage[y_pointer - 1, x_pointer]):
        queue.append((x_pointer, y_pointer + 1))
        # modImage[x_pointer, y_pointer + 1] = red

    # Left
    if all(modImage[y_pointer, x_pointer - 1]):
        queue.append((x_pointer - 1, y_pointer))
        # modImage[x_pointer - 1, y_pointer] = red

    # Down
    if all(modImage[y_pointer + 1, x_pointer]):
        queue.append((x_pointer, y_pointer - 1))
        # modImage[x_pointer, y_pointer - 1] = red

    # Right
    if all(modImage[y_pointer, x_pointer + 1]):
        queue.append((x_pointer + 1, y_pointer))
        # modImage[x_pointer + 1, y_pointer] = red

    counter = 0

    # Begin while loop
    while len(queue) and counter < counter_max:

        # movement = queue.pop(len(queue) - 1)
        movement = queue.pop(len(queue)-1)

        if checked[movement[0], movement[1]] == 0:
            x_pointer = movement[0]
            y_pointer = movement[1]

        else:
            continue

        # Mark current node as having been checked
        checked[x_pointer, y_pointer] = 1

        # Check if surrounding nodes are valid
        # If yes then add them to the queue in order U, L, D, R

        # Up
        if 0 <= y_pointer - 1 <= (size - 1) and 0 <= x_pointer <= (size - 1):
            if all(modImage[y_pointer - 1, x_pointer]) and checked[y_pointer - 1, x_pointer] == 0:
                queue.append((x_pointer, y_pointer - 1))
                # modImage[x_pointer, y_pointer + 1] = red

        # Left
        if 0 <= y_pointer <= (size - 1) and 0 <= x_pointer - 1 <= (size - 1):
            if all(modImage[y_pointer, x_pointer - 1]) and checked[y_pointer, x_pointer - 1] == 0:
                queue.append((x_pointer - 1, y_pointer))
                # modImage[x_pointer - 1, y_pointer] = red

        # Down
        if 0 <= y_pointer + 1 <= (size - 1) and 0 <= x_pointer <= (size - 1):
            if all(modImage[y_pointer + 1, x_pointer]) and checked[y_pointer + 1, x_pointer] == 0:
                queue.append((x_pointer, y_pointer + 1))
                # modImage[x_pointer, y_pointer - 1] = red

        # Right
        if 0 <= y_pointer <= (size - 1) and 0 <= x_pointer + 1 <= (size - 1):
            if all(modImage[y_pointer, x_pointer + 1]) and checked[y_pointer, x_pointer + 1] == 0:
                queue.append((x_pointer + 1, y_pointer))
                # modImage[x_pointer + 1, y_pointer] = red

        modImage[y_pointer, x_pointer] = red

        counter = counter + 1

        if x_pointer == end_location_x and y_pointer == end_location_y:
            return modImage

        # Loop

    return modImage


def bfs(modImage):

    # Create a pointer to check if end location is found
    x_pointer = start_location_x
    y_pointer = start_location_y

    # Create queue list
    queue = []

    # Create traversal list
    traversal = []

    # Create binary matrix to check if location has been checked
    checked = np.zeros((size, size))

    # Mark start position as checked
    checked[y_pointer, x_pointer] = 1

    # Find start location
    start_location = (x_pointer, y_pointer)
    traversal.append(start_location)

    # Determine connecting nodes from initial location and if they are valid targets
    # Load (append) them into the queue in order of U, L, D, R
    # Save as tuples of type (x, y), then store in list

    # Up
    if all(modImage[y_pointer - 1, x_pointer]):
        queue.append((x_pointer, y_pointer + 1))
        # modImage[x_pointer, y_pointer + 1] = red

    # Left
    if all(modImage[y_pointer, x_pointer - 1]):
        queue.append((x_pointer - 1, y_pointer))
        # modImage[x_pointer - 1, y_pointer] = red

    # Down
    if all(modImage[y_pointer + 1, x_pointer]):
        queue.append((x_pointer, y_pointer - 1))
        # modImage[x_pointer, y_pointer - 1] = red

    # Right
    if all(modImage[y_pointer, x_pointer + 1]):
        queue.append((x_pointer + 1, y_pointer))
        # modImage[x_pointer + 1, y_pointer] = red

    counter = 0

    # Begin while loop
    while len(queue) and counter < counter_max:
        # Check if next node in queue has been searched
        # If not, then pop queue
        # BFS uses pop, DFS uses popleft
        movement = queue.pop(0)

        if checked[movement[1], movement[0]] == 0:
            x_pointer = movement[0]
            y_pointer = movement[1]

        else:
            continue

        # Mark current node as having been checked
        checked[y_pointer, x_pointer] = 1

        # Check if surrounding nodes are valid
        # If yes then add them to the queue in order U, L, D, R

        # Up
        if 0 <= y_pointer - 1 <= (size - 1) and 0 <= x_pointer <= (size - 1):
            if all(modImage[y_pointer - 1, x_pointer]) and checked[y_pointer - 1, x_pointer] == 0:
                queue.append((x_pointer, y_pointer - 1))
                # modImage[x_pointer, y_pointer + 1] = red

        # Left
        if 0 <= y_pointer <= (size - 1) and 0 <= x_pointer - 1 <= (size - 1):
            if all(modImage[y_pointer, x_pointer - 1]) and checked[y_pointer, x_pointer - 1] == 0:
                queue.append((x_pointer - 1, y_pointer))
                # modImage[x_pointer - 1, y_pointer] = red

        # Down
        if 0 <= y_pointer + 1 <= (size - 1) and 0 <= x_pointer <= (size - 1):
            if all(modImage[y_pointer + 1, x_pointer]) and checked[y_pointer + 1, x_pointer] == 0:
                queue.append((x_pointer, y_pointer + 1))
                # modImage[x_pointer, y_pointer - 1] = red

        # Right
        if 0 <= y_pointer <= (size - 1) and 0 <= x_pointer + 1 <= (size - 1):
            if all(modImage[y_pointer, x_pointer + 1]) and checked[y_pointer, x_pointer + 1] == 0:
                queue.append((x_pointer + 1, y_pointer))
                # modImage[x_pointer + 1, y_pointer] = red

        if x_pointer == end_location_x and y_pointer == end_location_y:

            for x in range(len(traversal)):
                modImage[traversal[x][1], traversal[x][0]] = red

            return modImage

        # If there are currently no valid nodes to move to, backtrack to previous node
        # else:
        #     x_pointer = traversal[0][1]
        #     y_pointer = traversal[0][0]
        #     traversal.pop(0)

        # Add current position to traversal
        traversal.append((x_pointer, y_pointer))

        counter = counter + 1

        # Loop

    # Once end location has been reached color traversal list red
    for x in range(len(traversal)):
        modImage[traversal[x][1], traversal[x][0]] = red

    return modImage


def d_search(modImage):

    # Create traversal list
    traversal = []

    # Create queue list
    queue = []

    # Create distance list
    distances = []

    # Create pointers
    x_pointer = start_location_x
    y_pointer = start_location_y

    # Create binary matrix to check if location has been checked
    checked = np.zeros((size, size))

    # Mark start position as checked
    checked[y_pointer, x_pointer] = 1

    # Create a distance matrix
    distance_mat = np.zeros((size, size), dtype=float)

    # Populate the distance matrix
    for x in range(size):
        for y in range(size):
            distance_mat[y, x] = np.abs(np.sqrt(x**2 + y**2) - np.sqrt(start_location_x**2 + start_location_y**2))

    # Determine connecting nodes from initial location and if they are valid targets
    # Load (append) them into the queue in order of U, L, D, R
    # Save as tuples of type (x, y), then store in list

    # Up
    if all(modImage[y_pointer - 1, x_pointer]):
        queue.append((x_pointer, y_pointer - 1))
        distances.append(distance_mat[y_pointer - 1, x_pointer])
        # modImage[x_pointer, y_pointer + 1] = red

    # Left
    if all(modImage[y_pointer, x_pointer - 1]):
        queue.append((x_pointer - 1, y_pointer))
        distances.append(distance_mat[y_pointer, x_pointer - 1])
        # modImage[x_pointer - 1, y_pointer] = red

    # Down
    if all(modImage[y_pointer + 1, x_pointer]):
        queue.append((x_pointer, y_pointer + 1))
        distances.append(distance_mat[y_pointer + 1, x_pointer])
        # modImage[x_pointer, y_pointer - 1] = red

    # Right
    if all(modImage[y_pointer, x_pointer + 1]):
        queue.append((x_pointer + 1, y_pointer))
        distances.append(distance_mat[y_pointer, x_pointer + 1])
        # modImage[x_pointer + 1, y_pointer] = red

    counter = 0

    # Start loop
    while len(queue) and counter < counter_max:

        # Determine lowest cost move
        order_temp = np.argpartition(distances, len(distances) - 1)

        # Determine if location can be moved to
        distance_temp = distances.pop(order_temp[0])
        movement = queue.pop(order_temp[0])

        if checked[movement[1], movement[0]] == 0:
            x_pointer = movement[0]
            y_pointer = movement[1]

        else:
            continue

        # Mark current node as having been checked
        checked[y_pointer, x_pointer] = 1

        # Check if surrounding nodes are valid
        # If yes then add them to the queue in order U, L, D, R

        # Up
        if 0 <= y_pointer - 1 <= (size - 1) and 0 <= x_pointer <= (size - 1):
            if all(modImage[y_pointer - 1, x_pointer]) and checked[y_pointer - 1, x_pointer] == 0:
                queue.append((x_pointer, y_pointer - 1))
                distances.append(distance_mat[y_pointer - 1, x_pointer])
                # modImage[x_pointer, y_pointer + 1] = red

        # Left
        if 0 <= y_pointer <= (size - 1) and 0 <= x_pointer - 1 <= (size - 1):
            if all(modImage[y_pointer, x_pointer - 1]) and checked[y_pointer, x_pointer - 1] == 0:
                queue.append((x_pointer - 1, y_pointer))
                distances.append(distance_mat[y_pointer, x_pointer - 1])
                # modImage[x_pointer - 1, y_pointer] = red

        # Down
        if 0 <= y_pointer + 1 <= (size - 1) and 0 <= x_pointer <= (size - 1):
            if all(modImage[y_pointer + 1, x_pointer]) and checked[y_pointer + 1, x_pointer] == 0:
                queue.append((x_pointer, y_pointer + 1))
                distances.append(distance_mat[y_pointer + 1, x_pointer])
                # modImage[x_pointer, y_pointer - 1] = red

        # Right
        if 0 <= y_pointer <= (size - 1) and 0 <= x_pointer + 1 <= (size - 1):
            if all(modImage[y_pointer, x_pointer + 1]) and checked[y_pointer, x_pointer + 1] == 0:
                queue.append((x_pointer + 1, y_pointer))
                distances.append(distance_mat[y_pointer, x_pointer + 1])
                # modImage[x_pointer + 1, y_pointer] = red

        traversal.append((x_pointer, y_pointer))

        if x_pointer == end_location_x and y_pointer == end_location_y:

            for x in range(len(traversal)):
                modImage[traversal[x][1], traversal[x][0]] = red

            return modImage

        counter = counter + 1

    return modImage


def random_search(modImage):

    # Create traversal list
    traversal = []

    # Define start and end points
    start_location = (start_location_x, start_location_y)
    end_location = (end_location_x, end_location_y)

    # Add start location to traversal list
    traversal.append(start_location)

    # create pointer for current location
    x_pointer = start_location_x
    y_pointer = start_location_y

    counter = 0

    # Begin while loop
    while (x_pointer != end_location_x or y_pointer != end_location_y) and counter < counter_max:
        # Move
        # randomly choose which direction to move in
        movement = random.randint(0, 4)

        # Move up
        if movement == 1:
            if 0 <= y_pointer - 1 <= (size - 1) and 0 <= x_pointer <= (size - 1):
                if all(modImage[y_pointer - 1, x_pointer]):
                    y_pointer = y_pointer - 1

        # Move down
        if movement == 2:
            if 0 <= y_pointer + 1 <= (size - 1) and 0 <= x_pointer <= (size - 1):
                if all(modImage[y_pointer + 1, x_pointer]):
                    y_pointer = y_pointer + 1

        # Move left
        if movement == 3:
            if 0 <= y_pointer <= (size - 1) and 0 <= x_pointer - 1 <= (size - 1):
                if all(modImage[y_pointer, x_pointer - 1]):
                    x_pointer = x_pointer - 1

        # Move right
        if movement == 4:
            if 0 <= y_pointer <= (size - 1) and 0 <= x_pointer + 1 <= (size - 1):
                if all(modImage[y_pointer, x_pointer + 1]):
                    x_pointer = x_pointer + 1

        # Add current location to traversal list
        traversal.append((x_pointer, y_pointer))

        counter = counter + 1

        # Check if arrived at end

        # If yes, exit and paint

        # If no, loop

    for x in range(len(traversal)):
        modImage[traversal[x][1], traversal[x][0]] = red

    modImage[start_location_y, start_location_x] = green
    modImage[end_location_y, end_location_x] = blue

    return modImage


if __name__ == "__main__":
    # Create a blank/white array/image
    image = np.ones((size, size, 3), np.uint8)

    image = image * 255

    # Generate obstacles
    image = populateObstacles(image, coverage)

    image1 = image.copy()
    image2 = image.copy()
    image3 = image.copy()
    image4 = image.copy()

    # Breadth First Search
    bfs_image = bfs(image1)

    bfs_image[start_location_y, start_location_x] = green
    bfs_image[end_location_y, end_location_x] = blue

    # Depth First Search
    dfs_image = dfs(image2)

    dfs_image[start_location_y, start_location_x] = green
    dfs_image[end_location_y, end_location_x] = blue

    # Djikstra's Search
    d_image = d_search(image3)

    d_image[start_location_y, start_location_x] = green
    d_image[end_location_y, end_location_x] = blue

    # Random Search
    random_image = random_search(image4)

    random_image[start_location_y, start_location_x] = green
    random_image[end_location_y, end_location_x] = blue

    fig, grid = plt.subplots(2, 2)

    grid[0, 0].imshow(bfs_image)
    grid[0, 0].set_title('Breadth First Search')
    grid[0, 1].imshow(dfs_image)
    grid[0, 1].set_title('Depth First Search')
    grid[1, 0].imshow(d_image)
    grid[1, 0].set_title('Djikstra')
    grid[1, 1].imshow(random_image)
    grid[1, 1].set_title('Random Search')

    plt.show()
