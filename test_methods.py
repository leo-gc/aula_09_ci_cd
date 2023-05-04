import methods
 
def test_area():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the area
    output = methods.area_of_rectangle(width, height)

    # then the area should be 10
    assert output == 10
 
def test_perimeter():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the perimeter
    output = methods.perimeter_of_rectangle(width, height)
    
    # then the perimeter should be 14
    assert output == 14

def test_sum():
    # given the numbers 7 and 5
    a = 7
    b = 5

    # when we calculate the sum
    output = methods.sum(a, b)

    # then the result should be 12
    assert output == 12

def test_subtract():
    # given the numbers 7 and 5
    a = 7
    b = 5

    # when we calculate the difference
    output = methods.subtract(a, b)

    # then the result should be 2
    assert output == 2

def test_multiply():
    # given the numbers 7 and 5
    a = 7
    b = 5

    # when we calculate the product
    output = methods.multiply(a, b)

    # then the result should be 35
    assert output == 35

def test_divide():
    # given the numbers 35 and 5
    a = 35
    b = 5

    # when we calculate the quocient
    output = methods.divide(a, b)

    # then the output should be 7
    assert output == 7