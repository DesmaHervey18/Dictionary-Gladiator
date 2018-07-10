from random import randint


def new_gladiator(health, rage, damage_low, damage_high):
    '''(int, int, int int) -> {Dictionary}
    Returns a dictionary with 4 key-value pairs.
    return gladiator
    '''
    return {
        'health': health,
        'rage': rage,
        'damage_low': damage_low,
        'damage_high': damage_high
    }


def attack(attacker, defender):
    # Damage dealt is a random integer between the attacker's damage_low and damage_high
    low_damage = attacker.get('damage_low')
    high_damage = attacker.get('damage_high')
    hit = randint(low_damage, high_damage)
    # Each attack can hit normally or crit
    # Crit chance is the same as the attacker's rage (50 rage == 50% crit chance)
    probability = randint(1, 99)
    if probability < attacker['rage']:  # critical hit!
        # Critting doubles damage dealt
        health = defender['health'] - (2 * hit)
        defender['health'] = max(0, health)
        # If a gladiator crits, their rage is reset to 0
        attacker['rage'] = 0
    else:
        # If the gladiator hits normally, their rage is increased by 15
        health = defender['health'] - hit
        defender['health'] = max(0, health)
        rage = attacker['rage'] + 15
        attacker['rage'] = min(rage, 100)


def heal(gladiator):
    return None


def is_dead(gladiator):
    return None
