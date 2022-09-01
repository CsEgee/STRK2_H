import speeding_ticket as st


def test_high_speed():
    assert (st.traffipax(50, 90, 20) == True)


def test_low_speed():
    assert (st.traffipax(50, 55, 20) == False)
