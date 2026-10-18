# test_shipping.py
import pytest

from shipping import shipping_fee


# Rule 1: the weight must be more than 0 kg, otherwise ValueError.
# Block: weight <= 0. The edge is exactly 0 kg.
# FAILS for 0: the code breaks Rule 1, because it rejects only weight < 0.
@pytest.mark.parametrize("weight", [0, -1, -0.5])
def test_rule1_non_positive_weight_is_rejected(weight):
    with pytest.raises(ValueError, match="more than 0 kg"):
        shipping_fee(weight)


# Rule 2: up to 1 kg costs 40 baht. The edges are just above 0 and exactly 1 kg.
# FAILS for 1: the code breaks Rule 2, because exactly 1 kg is charged 60 baht.
@pytest.mark.parametrize("weight, expected", [
    (0.1, 40),   # just above the lower edge
    (0.5, 40),   # inside the block
    (1, 40),     # exactly 1 kg is still "up to 1 kg"
])
def test_rule2_up_to_1kg_costs_40(weight, expected):
    assert shipping_fee(weight) == expected


# Rule 3: more than 1 kg and up to 5 kg costs 60 baht.
@pytest.mark.parametrize("weight, expected", [
    (1.1, 60),   # just above 1 kg
    (3, 60),     # inside the block
    (5, 60),     # exactly 5 kg is still "up to 5 kg"
])
def test_rule3_over_1kg_up_to_5kg_costs_60(weight, expected):
    assert shipping_fee(weight) == expected


# Rule 4: more than 5 kg costs 60 plus 10 per started kg above 5 kg.
# FAILS for 5.2, 5.01 and 6.5: the code breaks Rule 4, because it counts only
# whole kilograms above 5 kg and ignores a started kilogram.
@pytest.mark.parametrize("weight, expected", [
    (5.2, 70),   # the example in the docstring
    (5.01, 70),  # a tiny bit above 5 kg already starts one kg
    (6, 70),     # exactly 1 kg above 5 kg is one started kg
    (6.5, 80),   # 1.5 kg above 5 kg is two started kg
    (10, 110),   # exactly 5 kg above 5 kg is five started kg
])
def test_rule4_over_5kg_adds_10_per_started_kg(weight, expected):
    assert shipping_fee(weight) == expected
