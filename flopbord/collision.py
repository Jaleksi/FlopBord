def withinBounds(x, y, radius):  # Check if bird is not out of screen
    return 0+radius < x < 600-radius and 0+radius < y < 600-radius


def hittingWall(birdCord, wallCord):  # Check if bird collides with obstacles
    if(wallCord[0] < birdCord[0] < wallCord[0]+wallCord[2] and
       wallCord[1] < birdCord[1] < wallCord[1]+wallCord[3]):
        return True
    return False


if(__name__ == "__main__"):
    pass
