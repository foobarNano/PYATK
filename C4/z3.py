from string import ascii_lowercase

def encode(message: str, key: int, alphabet: str = ascii_lowercase) -> str:
    alphabet = list(alphabet)
    wrap_index = len(alphabet)
    message = message.lower()
    encoded = list()

    for c in message:
        if not c.isalpha(): encoded.append(c)
        else: encoded.append(alphabet[(alphabet.index(c) + key) % wrap_index])

    return ''.join(encoded)

def decode(message: str, key: int, alphabet: str = ascii_lowercase) -> str:
    alphabet = list(alphabet)
    wrap_index = len(alphabet)
    message = message.lower()
    decoded = list()

    for c in message:
        if not c.isalpha(): decoded.append(c)
        else: decoded.append(alphabet[(alphabet.index(c) - key) % wrap_index])

    return ''.join(decoded)


pl_alphabet = 'aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż'
sample = 'Niech się dzieje wola nieba, z nią się zawsze zgadzać trzeba!'

print(f'Raw:     {sample}')
sample = encode(sample, 5, pl_alphabet)
print(f'Encoded: {sample}')
sample = decode(sample, 5, pl_alphabet)
print(f'Decoded: {sample}')
