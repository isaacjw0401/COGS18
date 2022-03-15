"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""

import pandas as pd
from functions import add_house
from functions import drop_house
from functions import find_house
from pandas.testing import assert_frame_equal
import mock   
df = pd.read_csv('property.csv')
##
##

def test_add_house():
    
    assert callable(add_house)
    
    house_add_initial = len(df.index)
    add_house(df)
    house_add_after = len(df.index)
    assert house_add_initial < house_add_after
    
    
    
def test_drop_house():
    
    assert callable(drop_house)
    
    house_drop_initial = len(df.index)
    drop_house(df)
    house_drop_after = len(df.index)
    assert house_drop_initial >= house_drop_after
     

        
#Referred to : https://stackoverflow.com/questions/51017249/what-is-the-difference-between-assert-frame-equal-and-equals

def test_find():
    
    assert callable(test_find)
    
    with mock.patch('builtins.input', side_effect=['1', '2000', '4']):
        assert_frame_equal(find_house(df), df.loc[df["BuiltYear"] >= 2000])
        
        
test_add_house()
test_drop_house()
test_find()