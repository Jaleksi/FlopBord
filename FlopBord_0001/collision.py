def collision(x1, y1, x2, y2, size1, size2):
    if(x1+size1 > x2 and x1-size1 < x2+size2):
        if(y1+size1 > y2 and y1-size1 < y2+size2):
            return True
    return False


def outOfBounds(x, y, radius):
    return 0+radius < x < 600-radius and 0+radius < y < 600-radius


if(__name__ == "__main__"):
    pass
