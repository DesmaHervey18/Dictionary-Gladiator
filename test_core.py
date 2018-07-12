from core import *


def test_new_gladiator():
    assert new_gladiator(20, 50, 70, 90) == {
        'health': 20,
        'rage': 50,
        'damage_low': 70,
        'damage_high': 90
    }
    assert new_gladiator(25, 55, 75, 100) == {
        'health': 25,
        'rage': 55,
        'damage_low': 75,
        'damage_high': 100
    }


def test_new_attack_no_rage():
    attacker = new_gladiator(100, 0, 10, 10)
    defender = new_gladiator(90, 55, 10, 20)
    attack(attacker, defender)
    assert attacker['rage'] == 15
    assert defender['health'] == 80


def test_new_attack_no_rage_dl_dh():
    attacker = new_gladiator(100, 0, 10, 30)
    defender = new_gladiator(90, 55, 10, 20)
    attack(attacker, defender)
    assert attacker['rage'] == 15
    assert defender['health'] >= 60 and defender['health'] <= 80


def test_new_attack_with_rage():
    attacker = new_gladiator(100, 100, 10, 10)
    defender = new_gladiator(90, 55, 10, 20)
    attack(attacker, defender)
    assert attacker['rage'] == 0
    assert defender['health'] == 70


# def test_new_heal():
#     assert heal(0, 5, 10, 15) == {
#         'health': 0,
#         'rage': 5,
#         'damage_low': 10,
#         'damage_high': 15
#     }


def test_is_dead():
    assert not is_dead({'health': 100})
    assert not is_dead({'health': 14})
    assert not is_dead({'health': 16})
    assert is_dead({'health': 0})


def test_attack():
    attack = {'health': 80, 'rage': 70, 'damage_low': 60, 'damage_high': 50}
    defender = {'health': 100, 'rage': 67, 'damage_low': 60, 'damage_high': 50}


def test_heal_10_health():
    attacker = new_gladiator(75, 60, 20, 20)
    heal(attacker)
    assert attacker['health'] == 80
    assert attacker['rage'] == 50


def test_heal_0_health():
    attacker = new_gladiator(85, 0, 30, 30)
    heal(attacker)
    assert attacker['health'] == 85
    assert attacker['rage'] == 0


def test_is_dead():
    assert is_dead({'health': 0})
    assert is_dead({'health': -1})
    assert not is_dead({'health': 100})
    assert not is_dead({'health': 1})
