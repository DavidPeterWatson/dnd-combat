from dnd_combat.dice import *
import pytest


def test_d4_roll():
    roll = roll_die(Die.d4)
    assert roll >= 1
    assert roll <= 4

def test_d3_roll_raises_exception():
    with pytest.raises(Exception):
        roll = roll_die(Die.d3)

def test_many_d4_rolls():
    for i in range(100):
        test_d4_roll()

def test_d6_roll():
    roll = roll_die(Die.d6)
    assert roll >= 1
    assert roll <= 6

def test_d8_roll():
    roll = roll_die(Die.d8)
    assert roll >= 1
    assert roll <= 8

def test_d10_roll():
    roll = roll_die(Die.d10)
    assert roll >= 1
    assert roll <= 10

def test_d12_roll():
    roll = roll_die(Die.d12)
    assert roll >= 1
    assert roll <= 12

def test_d20_roll():
    roll = roll_die(Die.d20)
    assert roll >= 1
    assert roll <= 20

def test_d100_roll():
    roll = roll_die(Die.d100)
    assert roll >= 1
    assert roll <= 100

def test_many_die_rolls():
    for i in range(1000):
        test_d4_roll()
        test_d6_roll()
        test_d8_roll()
        test_d10_roll()
        test_d12_roll()
        test_d20_roll()
        test_d100_roll()

def test_dice_type_roll():
    set_of_dice = SetOfDice(2, Die.d4)
    roll = roll_set_of_dice(set_of_dice)
    assert roll >= 2
    assert roll <= 8

def test_many_dice_Type_rolls():
    for i in range(1000):
        test_dice_type_roll()

def test_dice_roll():
    selection_of_dice = SelectionOfDice({SetOfDice(2, Die.d4), SetOfDice(2, Die.d4)}, lambda : 4)
    roll = roll_selection_of_dice(selection_of_dice)
    assert roll >= 8
    assert roll <= 20

def test_many_dice_rolls():
    for i in range(1000):
        test_dice_roll()
    