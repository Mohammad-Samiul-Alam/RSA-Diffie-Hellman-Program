# prime number -> n & phi (equations) -> keys(public & private)->message->blocks(3 digit)

# number -> key -> message -> blocks-> encryption -> decryption -> reconstruction
# RSA = Public Key Encryption.

# Step 1: Prime numbers(মৌলিক সংখ্যা)
p = 47
q = 71

# Step 2: Calculate n and phi
n = p * q
phi = (p - 1) * (q - 1)

# Step 3: Public and private keys
e = 79 #Public key
d = pow(e, -1, phi) #Private key ()

# Step 4: Original message
message = "6882326879666683"

# Step 5: Divide message into 3-digit blocks
blocks = [int(message[i:i+3]) for i in range(0, len(message), 3)] # [i:i+3] → Slicing
# ----------- OR --------------
# blocks = []

# for i in range(0, len(message), 3):
#     part = message[i:i+3]
#     blocks.append(int(part))
# ----------- OR --------------


# range(start, stop, step)
print("Original:", blocks)

# Step 6: Encryption
encrypted = [pow(m, e, n) for m in blocks]
print("Encrypted:", encrypted)

# Step 7: Decryption
decrypted = [pow(c, d, n) for c in encrypted]
print("Decrypted:", decrypted)

# Step 8: Reconstruct original message
result = ''.join(f"{m:03d}" for m in decrypted)
print("Original Message:", result)

