def atm_simulation():
    pin = "1234"
    balance = 100000
    tries = 3

    print("=== Welcome to Python ATM ===")

    # PIN verification
    while tries > 0:
        entered = input("Enter PIN: ")
        if entered == pin:
            print("PIN verified ✅\n")
            break
        tries -= 1
        print(f"Wrong PIN ❌  (Attempts left: {tries})")

    if tries == 0:
        print("Card blocked. Too many wrong attempts.")
        return

    # Main menu loop
    while True:
        print("\n--- ATM MENU ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Change PIN")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            print(f"Your balance is: ₹{balance:.2f}")

        elif choice == "2":
            amount = input("Enter deposit amount: ₹").strip()
            if not amount.replace('.', '', 1).isdigit():
                print("Invalid amount.")
                continue
            amount = float(amount)
            if amount <= 0:
                print("Amount must be greater than 0.")
                continue
            balance += amount
            print(f"Deposited ₹{amount:.2f}. New balance: ₹{balance:.2f}")

        elif choice == "3":
            amount = input("Enter withdraw amount: ₹").strip()
            if not amount.replace('.', '', 1).isdigit():
                print("Invalid amount.")
                continue
            amount = float(amount)
            if amount <= 0:
                print("Amount must be greater than 0.")
                continue
            if amount > balance:
                print("Insufficient balance ❌")
                continue
            balance -= amount
            print(f"Withdrawn ₹{amount:.2f}. New balance: ₹{balance:.2f}")

        elif choice == "4":
            old = input("Enter old PIN: ").strip()
            if old != pin:
                print("Incorrect old PIN ❌")
                continue
            new = input("Enter new PIN (4 digits): ").strip()
            if len(new) != 4 or not new.isdigit():
                print("PIN must be exactly 4 digits.")
                continue
            pin = new
            print("PIN changed successfully ✅")

        elif choice == "5":
            print("Thank you for using Python ATM. Goodbye 👋")
            break

        else:
            print("Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    atm_simulation()
