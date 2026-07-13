from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature

# -------------------------------------------------
# Step 1: Generate RSA Public and Private Keys
# -------------------------------------------------

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

public_key = private_key.public_key()

# -------------------------------------------------
# Step 2: Original Message
# -------------------------------------------------

message = "Hello Blockchain"

print("Original Message:")
print(message)

# -------------------------------------------------
# Step 3: Generate SHA-256 Hash
# -------------------------------------------------

message_hash = hashlib.sha256(message.encode()).hexdigest()

print("\nSHA-256 Hash:")
print(message_hash)

# -------------------------------------------------
# Step 4: Generate Digital Signature
# -------------------------------------------------

signature = private_key.sign(
    message.encode(),
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

print("\nDigital Signature (Hex):")
print(signature.hex())

# -------------------------------------------------
# Step 5: Verify Digital Signature
# -------------------------------------------------

try:
    public_key.verify(
        signature,
        message.encode(),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    print("\nVerification Successful")
    print("The message is authentic.")
    print("The message has not been modified.")

except InvalidSignature:

    print("\nVerification Failed")
    print("The signature is invalid.")