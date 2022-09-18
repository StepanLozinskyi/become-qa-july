def test_lists():
    # if [1, 2, 3] != [1, 2, 3]
    #     raise AssertionError("Not equal")
    # identical to \/
    assert [1, 2, 3] == [1, 2, 3]

#def test_lists_fail():
#    assert [1, 3, 3] == [1, 2, 3]

def test_lists_ok():
    assert [1, 3, 3] != [1, 2, 3]