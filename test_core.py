 gladiator = {
        'health': health,
        'rage': rage,
        'damage_low': damage_low,
        'damage_high': damage_high
    }
    return gladiator

def test_new_gladiator():
    assert test_new_gladiator(25, 50, 75, 100) == {
        'health': 25,
        'rage': 50,
        'damage_low': 75,
        'damage_high': 100
        }

        assert test_attack(20, 40, 60, 80) == {
        'health': 20,
        'rage': 40,
        'damage_low': 60,
        'damage_high': 80
        }

        assert test_heal(0, 5, 10, 15) == {
        'health': 0,
        'rage': 5,
        'damage_low': 10,
        'damage_high': 15
        }

def test_is_dead():
    assert is_dead(12, 14, 16, 18) == {
    assert not is_dead({'health': 12}),
    assert is_dead({'rage': 14}),
    assert not is_dead({'damage_low': 16}),
    assert is_dead({'damage_high': 18})
    }
    
def test_attack(): 
    attack = {'health':80, 'rage':70, 'damage_low':60, 'damage_high':50}
    defender = {'health':100, 'rage':67, 'damage_low':60, 'damage_high':50}
