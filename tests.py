from flopbord.collision import withinBounds

def testBounds():
    assert withinBounds(999, 999, 10) == False
    assert withinBounds(300, 300, 10) == True

if(__name__ == "__main__"):
    if(testBounds() is None):
        print("Tested withinBounds, no errors")
