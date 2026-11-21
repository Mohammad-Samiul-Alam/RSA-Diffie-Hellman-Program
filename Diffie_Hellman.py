# Diffie-Hellman : Secret Key Sharing.

# Public Values
p = 353                 # Prime number
g = 3                   # Primitive root

# Primitive Root (সহজ ভাষায়):
# যে সংখ্যা দিয়ে একটি Prime Number-এর সব non-zero remainder তৈরি করা যায়, তাকে Primitive Root বলে।
# Shortcut: Primitive Root = Generator (g).

# Private Keys
a = 97                  # Alice's private key
b = 233                 # Bob's private key

# Generate Public Keys
A = pow(g, a, p)        # Alice's public key = g^a mod p
B = pow(g, b, p)        # Bob's public key = g^b mod p

# Generate Shared Secret Keys
alice_key = pow(B, a, p)  # Alice's shared key = B^a mod p
bob_key = pow(A, b, p)    # Bob's shared key = A^b mod p

# Display Public Keys
print("Alice Public Key:", A)  # Print Alice's public key
print("Bob Public Key:", B)    # Print Bob's public key

# Display Shared Keys
print("Alice Shared Key:", alice_key)  # Print Alice's shared key
print("Bob Shared Key:", bob_key)      # Print Bob's shared key

# Check Shared Keys
if alice_key == bob_key:              # Compare both keys
    print("Key Exchange Successful!") # If keys are equal
else:
    print("Key Exchange Failed!")     # If keys are different