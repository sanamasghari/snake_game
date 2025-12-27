from main import head_angle, vali_snake_direction, valid_fruit_location
import pytest


def test_is_valid_direction():
    assert vali_snake_direction('') == False
    assert vali_snake_direction("cat") == False
    assert vali_snake_direction('up') == True
    assert vali_snake_direction(5) == False
    

def test_snake_head_angle():
    assert head_angle("up") == 180
    assert head_angle("down") ==  0
    assert head_angle("left") ==  270
    assert head_angle("right") ==  90  
    
    with pytest.raises(KeyError):
        head_angle('')
        
        
def test_is_valid_fruit_location():
    assert valid_fruit_location(20,10) == "out side of the map"
    assert valid_fruit_location(10,20) == "out side of the map"
    assert valid_fruit_location(17,15) == "food is on the margin"
    assert valid_fruit_location(1,17) == "food is on the margin"
    assert valid_fruit_location(5,12) == "right place"
    
    