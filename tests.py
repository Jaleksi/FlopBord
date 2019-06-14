from flopbord.collision import withinBounds, hittingWall

def testBounds():
    assert withinBounds(999, 999, 10) == False
    assert withinBounds(300, 300, 10) == True

def testWall():
    assert hittingWall([300, 300], [400, 0, 80, 400]) == False
    assert hittingWall([450, 300], [400, 0, 80, 400]) == True

if(__name__ == "__main__"):
    if(testBounds() is None):
        print("Tested withinBounds, no errors")
    if(testWall() is None):
        print("Tested hittingWall, no errors")
