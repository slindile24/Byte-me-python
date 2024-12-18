import csv

DATABASE_FILE = "banking_app/database.csv"

def read_users():
    """Reads all users from the CSV database and returns a list of dictionaries."""
    users = []
    try:
        with open(DATABASE_FILE, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                users.append({
                    "username": row["username"],
                    "password": row["password"],
                    "email": row["email"],
                    "account_id": row["account_id"],
                    "balance": float(row["balance"]),  
                })
    except FileNotFoundError:
        raise FileNotFoundError(f"Database file '{DATABASE_FILE}' not found.") # except this error in your code
    return users

def write_users(users):
    """Writes the updated user list back to the CSV database."""
    try:
        with open(DATABASE_FILE, mode='w', newline='') as file:
            fieldnames = ["username", "password", "email", "account_id", "balance"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for user in users:
                writer.writerow({
                    "username": user["username"],
                    "password": user["password"],
                    "email": user["email"],
                    "account_id": user["account_id"],
                    "balance": f"{user['balance']:.2f}", 
                })
    except Exception as e:
        raise RuntimeError(f"Failed to write to database: {str(e)}") # except this error in your code
