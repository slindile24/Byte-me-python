# transaction.py - Placeholder for transaction functionality

def transact(sender_account, receiver_account, amount):
    """
    Handles the transfer of funds between two user accounts.

    Instructions for Implementation:
    1. **Input Validation**:
        - Ensure that both `sender_account` and `receiver_account` are non-empty strings.
        - Ensure that the `amount` is a positive number greater than zero.
        - If the `amount` is less than or equal to zero, raise a `ValueError`.
        - If the `sender_account` and `receiver_account` are the same, raise a `ValueError`.

    2. **Account Validation**:
        - Check if both the `sender_account` and `receiver_account` exist in the user database.
        - If either account is invalid (does not exist), raise a `ValueError`.

    3. **Balance Check**:
        - Check if the `sender_account` has enough funds to complete the transaction.
        - If the balance is insufficient (i.e., the balance is less than the `amount`), raise a `ValueError`.

    4. **Transaction Execution**:
        - Deduct the specified `amount` from the `sender_account`.
        - Add the `amount` to the `receiver_account`.
        - Update the user database to reflect the new balances.

    5. **Edge Cases**:
        - Ensure that invalid or insufficient funds do not complete the transaction.
        - Ensure that the `amount` is always positive and non-zero.
        - Ensure that the `sender_account` cannot be the same as the `receiver_account`.
        - Handle cases where either of the accounts does not exist in the database.

    Parameters:
    - `sender_account` (str): The account ID of the user sending the funds.
    - `receiver_account` (str): The account ID of the user receiving the funds.
    - `amount` (float): The amount of money to be transferred.

    Returns:
    - bool: `True` if the transaction is successfully completed, `False` otherwise.

    Raises:
    - ValueError: If the `amount` is negative or zero, or if either of the accounts is invalid, or if there are insufficient funds in the `sender_account`, or if the sender and receiver are the same.

    """

    #hint should use read_users and write_users from user_management

