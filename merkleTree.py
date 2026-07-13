import hashlib


# Function to compute SHA-256 hash
def sha256(data):
    return hashlib.sha256(data.encode()).hexdigest()


# Build the Merkle Tree
def build_merkle_tree(transactions):
    tree = []
    current_level = [sha256(tx) for tx in transactions]
    tree.append(current_level)

    while len(current_level) > 1:
        if len(current_level) % 2 != 0:
            current_level.append(current_level[-1])

        next_level = []
        for i in range(0, len(current_level), 2):
            combined = current_level[i] + current_level[i + 1]
            next_level.append(sha256(combined))

        tree.append(next_level)
        current_level = next_level

    return tree


# Generate Membership Proof
def generate_proof(tree, index):
    proof = []

    for level in tree[:-1]:
        if len(level) % 2 != 0:
            level = level + [level[-1]]

        if index % 2 == 0:
            sibling = level[index + 1]
            direction = "right"
        else:
            sibling = level[index - 1]
            direction = "left"

        proof.append((sibling, direction))
        index //= 2

    return proof


# Verify Membership Proof
def verify_proof(transaction, proof, merkle_root):
    current_hash = sha256(transaction)

    for sibling_hash, direction in proof:
        if direction == "right":
            current_hash = sha256(current_hash + sibling_hash)
        else:
            current_hash = sha256(sibling_hash + current_hash)

    return current_hash == merkle_root


# ---------------------- MAIN PROGRAM ----------------------

transactions = [
    "Alice pays Bob 10 BTC",
    "Bob pays Charlie 5 BTC",
    "Charlie pays David 2 BTC",
    "David pays Eve 1 BTC"
]

tree = build_merkle_tree(transactions)
merkle_root = tree[-1][0]

print("Merkle Root:")
print(merkle_root)

# Membership Proof
transaction = "Bob pays Charlie 5 BTC"

if transaction in transactions:
    index = transactions.index(transaction)
    proof = generate_proof(tree, index)

    print("\nMembership Proof:")
    for p in proof:
        print(p)

    if verify_proof(transaction, proof, merkle_root):
        print("\nResult: Transaction EXISTS in the Merkle Tree.")
    else:
        print("\nResult: Verification FAILED.")
else:
    print("\nTransaction not found.")

# Non-membership Check
fake_transaction = "Alice pays John 100 BTC"

print("\nChecking Non-membership:")

if fake_transaction in transactions:
    print("Transaction exists.")
else:
    print("Transaction DOES NOT exist in the Merkle Tree.")