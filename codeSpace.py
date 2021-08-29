# binary to decimal without using built-in method int()
def decimal(binary):
    sz = len(binary)
    dec, index = 0, sz-1

    for bit in binary:
        if bit == '1':
            dec += pow(2, index)
        index -= 1

    return dec

# decimal to binary without using built-in method bin()
def binary(decimal):
    _bin = []

    while decimal > 0:
        _bin.append(str(decimal % 2))
        decimal //= 2

    b = ""

    for bit in reversed(_bin):
        b += bit

    return b


_input = input("Enter input type (b/d): ").lower()

if _input == 'b':
    print(f"Decimal: {decimal(input('Enter a binary value: '))}")
else:
    print(f"Binary: {binary(int(input('Enter a decimal value : ')))}")
