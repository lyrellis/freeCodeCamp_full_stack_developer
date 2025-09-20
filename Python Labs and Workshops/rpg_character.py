full_dot = '●'
empty_dot = '○'


# Create an RPG character
def create_character(character_name, strength, intelligence, charisma):
    
    # Validate character_name
    if not isinstance(character_name, str):
        return 'The character name should be a string'
    elif len(character_name) > 10:
        return 'The character name is too long'
    elif ' ' in character_name:
        return 'The character name should not contain spaces'
    
    # Validate stats
    if not isinstance(strength, int) or not isinstance(intelligence, int) or not isinstance(charisma, int):
        return 'All stats should be integers'
    elif strength < 1 or intelligence < 1 or charisma < 1:
        return 'All stats should be no less than 1'
    elif strength > 4 or intelligence > 4 or charisma > 4:
        return 'All stats should be no more than 4'
    elif strength + intelligence + charisma != 7:
        return 'The character should start with 7 points'
    
    # Format an output string
    string_out = character_name + '\n'
    string_out += 'STR ' +full_dot*strength + empty_dot*(10-strength) + '\n'
    string_out += 'INT ' + full_dot*intelligence + empty_dot*(10-intelligence) + '\n' 
    string_out += 'CHA ' + full_dot*charisma + empty_dot*(10-charisma)

    # Return output string
    return string_out

if __name__=='__main__':
    # Example
    print(create_character('ren', 4, 2, 1))
