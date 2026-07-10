import logging

logging.basicConfig(
    filename="transacation.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Custom Exception
class InvalidTransactionError(Exception):
    """Custom Exception"""

    pass

def payment():
    """
    Processes a payment transaction.
    Raises:
        InvalidTransactionError:
            - If the entered amount is negative
            - If the entered amount exceeds account balance
        Logs:
        Error details with timestamp and transaction ID
        into the transaction.log file.
    """

    transaction_id = input("Enter Transaction Id: ")
    amount = int(input("Enter Amount: "))

    balance = 10000

    try:
        if amount < 0:
            raise InvalidTransactionError("Invalid Amount")

        if amount > balance:
            raise InvalidTransactionError("Insufficient Balance")

        print(f"Transaction {transaction_id}: {amount} Successful!!!!")

    except InvalidTransactionError as e:
        logging.error(f"Transaction Id: {transaction_id} - {e}")
        print(f"Transaction {transaction_id} Failed")

payment()
