import math
from app.physics import decay_constant, quantity_remaining, time_until_quantity, decay_curve_points

def test_decay_constant():
    # Test with a known half-life
    halflife = 10.0  # seconds
    expected_lambda = math.log(2) / halflife
    assert math.isclose(decay_constant(halflife), expected_lambda)

    # Test with zero half-life (should raise ValueError)
    try:
        decay_constant(0)
        assert False, "Expected ValueError for zero half-life"
    except ValueError:
        pass

    # Test with negative half-life (should raise ValueError)
    try:
        decay_constant(-5)
        assert False, "Expected ValueError for negative half-life"
    except ValueError:
        pass

def test_quantity_remaining():
    initial_amount = 100.0
    halflife = 10.0
    time = 20.0
    expected_remaining = initial_amount * math.exp(-decay_constant(halflife) * time)
    assert math.isclose(quantity_remaining(initial_amount, halflife, time), expected_remaining)

    # Test with zero initial amount (should return 0)
    assert quantity_remaining(0, halflife, time) == 0

    # Test with negative initial amount (should raise ValueError)
    try:
        quantity_remaining(-10, halflife, time)
        assert False, "Expected ValueError for negative initial amount"
    except ValueError:
        pass

    # Test with zero half-life (should raise ValueError)
    try:
        quantity_remaining(initial_amount, 0, time)
        assert False, "Expected ValueError for zero half-life"
    except ValueError:
        pass

    # Test with negative time (should raise ValueError)
    try:
        quantity_remaining(initial_amount, halflife, -5)
        assert False, "Expected ValueError for negative time"
    except ValueError:
        pass

def test_time_until_quantity():
    initial_amount = 100.0
    halflife = 10.0
    final_amount = 25.0
    expected_time = math.log(initial_amount / final_amount) / decay_constant(halflife)
    assert math.isclose(time_until_quantity(initial_amount, halflife, final_amount), expected_time)

    # Test with zero initial amount (should raise ValueError)
    try:
        time_until_quantity(0, halflife, final_amount)
        assert False, "Expected ValueError for zero initial amount"
    except ValueError:
        pass

    # Test with negative initial amount (should raise ValueError)
    try:
        time_until_quantity(-10, halflife, final_amount)
        assert False, "Expected ValueError for negative initial amount"
    except ValueError:
        pass

    # Test with zero half-life (should raise ValueError)
    try:
        time_until_quantity(initial_amount, 0, final_amount)
        assert False, "Expected ValueError for zero half-life"
    except ValueError:
        pass

    # Test with final amount greater than or equal to initial amount (should raise ValueError)
    try:
        time_until_quantity(initial_amount, halflife, initial_amount)
        assert False, "Expected ValueError for final amount >= initial amount"
    except ValueError:
        pass