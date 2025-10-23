''' A basic Caesar Cipher
'''
def caesar(text: str, shift: int, encrypt_: bool = True):
    ''' A Caesar Cipher function that takes an input string
    and either encrytps or decrypts that input using a given shift value.

    Parameters:
        text: (str)
            Input string

        shift: (int)
            Caesar shift value

        encrypt_: (bool)
            Defines whether to encrypt/decrypt the input string.
            A True value will cause the function to encrypt the text.
            A False values will cause the function to decrypt the text.
            The default value is set to True.

    Returns:
        shifted_text: (str)
            Outputs the inut text shifted by the given shift value.
    '''
    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt_:
        shift = - shift

    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(
        alphabet + alphabet.upper(),
        shifted_alphabet + shifted_alphabet.upper()
    )
    shifted_text = text.translate(translation_table)
    return shifted_text

def encrypt(text: str, shift: int):
    ''' Calls the caesar function to encrypt the input text.
    '''
    return caesar(text, shift)

def decrypt(text: str, shift: int):
    ''' Calls the caesar function to decrypt the input text.
    '''
    return caesar(text, shift, encrypt_ = False)

if __name__ == '__main__':
    # Example Decryption
    ENCRYPTED_TEXT = 'Pbhentr vf sbhaq va hayvxryl cynprf.'
    decrypted_text = decrypt(ENCRYPTED_TEXT, 13)
    print(decrypted_text)
