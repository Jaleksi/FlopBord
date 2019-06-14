def withinBounds(x, y, radius):
    return 0+radius < x < 600-radius and 0+radius < y < 600-radius


def hittingWall(birdCord, wallCord):
    if(wallCord[0]+wallCord[2] > birdCord[0] > wallCord[0] and
       wallCord[1]+wallCord[3] > birdCord[1] > wallCord[1]):
        return True
    return False


if(__name__ == "__main__"):
    pass
