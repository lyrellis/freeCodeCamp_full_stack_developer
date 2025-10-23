''' Create a rpg characer stat sheet
'''

# Store these symbols for later use
FULL_DOT = '●'
EMPTY_DOT = '○'

# Create an RPG character
def create_character(character_name: str, strength: int, intelligence: int, charisma: int):
    ''' A function that takes a character name and stats,
        validates them, 
        and formats a visual representation of those stats.
    '''
    # Validation begins
    invalid_criteria: list = []

    # Validate character_name
    if not isinstance(character_name, str):
        invalid_criteria.append('The character name should be a string')
    if len(character_name) > 10:
        invalid_criteria.append('The character name is too long')
    if ' ' in character_name:
        invalid_criteria.append('The character name should not contain spaces')

    # Validate stats
    if not all([
        isinstance(strength, int),
        isinstance(intelligence, int),
        isinstance(charisma, int)
    ]):
        invalid_criteria.append('All stats should be integers')
    try:
        if strength < 1 or intelligence < 1 or charisma < 1:
            invalid_criteria.append('All stats should be no less than 1')
        if strength > 4 or intelligence > 4 or charisma > 4:
            invalid_criteria.append('All stats should be no more than 4')
        if strength + intelligence + charisma != 7:
            invalid_criteria.append('The character should start with 7 points')
    except TypeError:
        pass

    if invalid_criteria:
        return '\n'.join(invalid_criteria)
    # Validation ends

    # Format an output string
    string_out: str = character_name + '\n'
    string_out += 'STR ' + FULL_DOT*strength + EMPTY_DOT*(10-strength) + '\n'
    string_out += 'INT ' + FULL_DOT*intelligence + EMPTY_DOT*(10-intelligence) + '\n'
    string_out += 'CHA ' + FULL_DOT*charisma + EMPTY_DOT*(10-charisma)

    return string_out

if __name__=='__main__':
    # Example
    print(create_character('ren', 4, 'x', 1))
