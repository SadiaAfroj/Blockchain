from bitcoinlib.keys import Key
from bitcoinlib.transactions import Transaction

sender_key=Key()
receiver_key=Key()

print("Sender Address: ",sender_key.address())
print("Receiver Address: ",receiver_key.address())

previous_tx=Transaction()
previous_tx.add_output(
    value=200,
    address=sender_key.address()
)
previous_txid=previous_tx.txid

initial_balance=previous_tx.outputs[0].value

tx=Transaction()
tx.add_input(
    prev_txid=previous_txid,
    output_n=0
)
sent_amount=100
tx.add_output(
    value=sent_amount,
    address=receiver_key.address()
)

if sent_amount>initial_balance:
    print("Insufficient balance")
    valid_amount=False
else:
    remaining_balance=initial_balance-sent_amount
    print("Remaining balance: ",remaining_balance)
    valid_amount=True

tx.sign(sender_key)

try:
    valid_signature=tx.verify()

    if valid_signature:
        print("Signature is valid")
    else:
        print("Signature is invalid")
except Exception as e:
    valid_signature=False
    print("verification failed")

expected_address=receiver_key.address()
actual_address=tx.outputs[0].address

if expected_address==actual_address:
    valid_address=True
    print("Address is valid")
else:
    valid_address=False
    print("Address is invalid")

if valid_address and valid_signature and valid_amount:
    print("TRansaction is valid")
else:
    print("Transaction is invalid")


tempering_amount=150

tx.outputs[0].value=150

try:
    tempered_result=tx.verify()

    if tempered_result:
        print("tempered transaction is valid")
    else:
        print("tempered transaction is invalid")
except Exception as e:
    tempered_result=False
    print("tempered transaction verification failed")