def withinBounds(x, y, radius):
    return 0+radius < x < 600-radius and 0+radius < y < 600-radius


def hittingWall(birdCord, wallCord):
    if(wallCord[0] < birdCord[0] < wallCord[0]+wallCord[2] and
       wallCord[1] < birdCord[1] < wallCord[1]+wallCord[3]):
        return True
    return False

# birdCord[0] = x, birdCord[1] = y
# wallCord[0] = x, wallCord[1] = y, ...[2] = leveys, ... [3] = korkeus


if(__name__ == "__main__"):
    pass
