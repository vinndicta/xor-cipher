def convert_to_binary(entry):
    entry_b = ''
    for e in entry:
        entry_b += format(ord(e), '08b')
    return entry_b

# i know that python has a built-in xor operation method, i wanted to use my own
def xor(k_bit, m_bit):
    if k_bit == m_bit:
        return 0 # 0 ⊕ 0 = 0    |   1 ⊕ 1 = 0
    else:
        return 1  # 1 ⊕ 0 = 1   |    0 ⊕ 1 = 1

def x_cipher(key_b, msg_b):
    cipher = ''
    for bit in range(len(msg_b)):
        cipher += str(xor(int(key_b[bit]), int(msg_b[bit])))
    return cipher

def main():
    key = input("\nKey: ")
    msg = input("Message: ")

    k_bin = input("Is your key in binary format? (y/n): ")

    if k_bin == 'n':
        key_b = convert_to_binary(key)
    else:
        key_b = key

    # express the message to a binary representation
    msg_b = convert_to_binary(msg)

    if len(key_b) > len(msg_b): # if the key is longer than the message...
            key_b = key_b[:len(msg_b)] # ...we truncate the key to match the latter's length
    else: # we make sure the key is the same length as the message
        while len(key_b) < len(msg_b):
            for i in range(len(key_b)):
                key_b += key_b[i]

    print(f"\nCipher : {x_cipher(key_b, msg_b)}\n")

if __name__ == "__main__":
    main()
