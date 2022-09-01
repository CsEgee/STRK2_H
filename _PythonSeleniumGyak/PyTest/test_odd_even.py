
import odd_even

def test_odd():
    b = odd_even.odd_even(5)
    assert(b == True)

def test_even():
    b = odd_even.odd_even(8)
    assert(b == False)

