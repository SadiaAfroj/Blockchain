import hashlib


# ============================================================
# 1. BLOCK
# ============================================================

class Block:

    def __init__(self, data, previous_hash):
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        text = self.data + self.previous_hash
        return hashlib.sha256(text.encode()).hexdigest()


# ============================================================
# 2. BLOCKCHAIN
# ============================================================

class Blockchain:

    def __init__(self):
        self.chain = [self.create_genesis_block()]

    # Create first block
    def create_genesis_block(self):
        return Block("Genesis Block", "0")

    # Add a new block
    def add_block(self, data):

        previous_hash = self.chain[-1].hash

        new_block = Block(data, previous_hash)

        self.chain.append(new_block)

    # Check whether blockchain is valid
    def validate_chain(self):

        for i in range(1, len(self.chain)):

            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check current block hash
            if current_block.hash != current_block.calculate_hash():
                print("Invalid hash at block", i)
                return False

            # Check connection with previous block
            if current_block.previous_hash != previous_block.hash:
                print("Invalid previous hash at block", i)
                return False

        print("Blockchain is valid")
        return True

    # Get number of blocks
    def get_chain_length(self):
        return len(self.chain)

    # Calculate simplified total hash value
    def get_chain_hashrate(self):

        total_hashrate = 0

        for block in self.chain:
            total_hashrate += int(block.hash, 16)

        return total_hashrate

    # Check for 51% attack
    def check_for_51_percent_attack(self):

        chain_length = self.get_chain_length()

        total_hashrate = self.get_chain_hashrate()

        for i in range(chain_length):

            block_hash = int(self.chain[i].hash, 16)

            percentage = block_hash / total_hashrate

            print(
                "Block", i,
                "share:",
                round(percentage * 100, 2),
                "%"
            )

            if percentage > 0.51:

                print("51% attack detected at block", i)

                return True

        print("No 51% attack detected")

        return False


# ============================================================
# 3. CREATE BLOCKCHAIN
# ============================================================

blockchain = Blockchain()


# Add blocks
blockchain.add_block("Transaction 1")
blockchain.add_block("Transaction 2")
blockchain.add_block("Transaction 3")


# ============================================================
# 4. DISPLAY BLOCKCHAIN
# ============================================================

print("=" * 60)
print("BLOCKCHAIN")
print("=" * 60)

for i, block in enumerate(blockchain.chain):

    print("\nBlock:", i)
    print("Data:", block.data)
    print("Previous Hash:", block.previous_hash)
    print("Hash:", block.hash)


# ============================================================
# 5. VALIDATE BLOCKCHAIN
# ============================================================

print("\n" + "=" * 60)
print("BLOCKCHAIN VALIDATION")
print("=" * 60)

blockchain.chain[1].data = "HACKED"
blockchain.validate_chain()


# ============================================================
# 6. CHECK 51% ATTACK
# ============================================================

print("\n" + "=" * 60)
print("51% ATTACK CHECK")
print("=" * 60)

blockchain.check_for_51_percent_attack()