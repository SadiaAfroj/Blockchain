import hashlib
import time


# Function for MD5
def md5_hash(message):
    return hashlib.md5(message.encode()).hexdigest()


# Function for SHA-256
def sha256_hash(message):
    return hashlib.sha256(message.encode()).hexdigest()


# Function to check properties
def verify_hash(algorithm, hash_function):

    print("\n============================")
    print(algorithm, "Verification")
    print("============================")


    # 1. Deterministic Property
    print("\n1. Deterministic Property")

    msg = "Hello World"

    h1 = hash_function(msg)
    h2 = hash_function(msg)

    print("First Hash :", h1)
    print("Second Hash:", h2)

    print("Result:", h1 == h2)


    # 2. Fast Computation
    print("\n2. Fast Computation")

    data = "Blockchain" * 100000

    start = time.time()

    hash_function(data)

    end = time.time()

    print("Execution Time:", end-start, "seconds")


    # 3. Pre-image Resistance
    print("\n3. Pre-image Resistance")

    secret = "password123"

    hashed_value = hash_function(secret)

    print("Hash:", hashed_value)

    print("Cannot find original input from hash easily")


    # 4. Second Pre-image Resistance
    print("\n4. Second Pre-image Resistance")

    original = "Data"

    another = "Data1"


    hash1 = hash_function(original)
    hash2 = hash_function(another)


    print("Original Hash :", hash1)
    print("New Hash      :", hash2)


    if hash1 != hash2:
        print("No second input with same hash")


    # 5. Collision Resistance
    print("\n5. Collision Resistance")

    messages = ["cat", "dog", "bird", "fish"]

    result = {}

    collision = False


    for m in messages:

        h = hash_function(m)

        print(m, ":", h)


        if h in result:
            collision = True

        result[h] = m


    if collision:
        print("Collision detected")
    else:
        print("No collision detected")


    # 6. Avalanche Effect
    print("\n6. Avalanche Effect")


    a = "Apple"
    b = "apple"


    hash_a = hash_function(a)
    hash_b = hash_function(b)


    print("Apple :", hash_a)
    print("apple :", hash_b)


    print("Small change creates completely different hash")


# Testing MD5
verify_hash("MD5", md5_hash)


# Testing SHA-256
verify_hash("SHA-256", sha256_hash)