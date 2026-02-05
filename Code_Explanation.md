# 📖 ATM Simulation Code Walkthrough

This document explains the `ATM_simulation.py` code step by step.

---

## Step 1: Function Definition & Initial Setup (Lines 1-4)

```python
def atm_simulation():
    pin = "1234"
    balance = 5000.0
    tries = 3
```

| Variable | Purpose |
|----------|---------|
| `pin = "1234"` | Default PIN code for the ATM |
| `balance = 5000.0` | Initial account balance of ₹5000 |
| `tries = 3` | Number of attempts allowed to enter correct PIN |

---

## Step 2: PIN Verification (Lines 6-19)

```python
print("=== Welcome to Python ATM ===")

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
```

### How It Works:
- **`while tries > 0:`** - Loop runs as long as attempts remain
- **`if entered == pin:`** - Check if entered PIN matches stored PIN
- **`break`** - Exit loop on correct PIN
- **`tries -= 1`** - Decrease remaining attempts on wrong PIN
- **`return`** - Ends the function if all attempts exhausted (card blocked)

---

## Step 3: Main Menu Loop (Lines 22-30)

```python
while True:
    print("\n--- ATM MENU ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Change PIN")
    print("5. Exit")

    choice = input("Choose an option (1-5): ").strip()
```

- **`while True:`** - Infinite loop that keeps showing the menu until user exits
- **`.strip()`** - Removes any extra whitespace from user input

---

## Step 4: Option 1 - Check Balance (Lines 32-33)

```python
if choice == "1":
    print(f"Your balance is: ₹{balance:.2f}")
```

- Simply displays the current balance
- **`:.2f`** formats the number to 2 decimal places (e.g., `5000.00`)

---

## Step 5: Option 2 - Deposit (Lines 35-45)

```python
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
```

### Validation Steps:

| Check | Purpose |
|-------|---------|
| `.replace('.', '', 1).isdigit()` | Validates input is a number (allows one decimal point) |
| `amount <= 0` | Ensures positive deposit amount |
| `continue` | Skips back to menu if validation fails |
| `balance += amount` | Adds deposit to balance |

---

## Step 6: Option 3 - Withdraw (Lines 47-60)

```python
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
```

### Key Points:
- Same validation as deposit
- **Extra check:** `amount > balance` prevents overdrawing
- **`balance -= amount`** subtracts from balance

---

## Step 7: Option 4 - Change PIN (Lines 62-72)

```python
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
```

### Security Checks:

| Check | Purpose |
|-------|---------|
| `old != pin` | Verify old PIN before allowing change |
| `len(new) != 4` | New PIN must be exactly 4 characters |
| `not new.isdigit()` | New PIN must contain only digits |

---

## Step 8: Option 5 - Exit (Lines 74-76)

```python
elif choice == "5":
    print("Thank you for using Python ATM. Goodbye 👋")
    break
```

- **`break`** exits the `while True` loop, ending the program

---

## Step 9: Invalid Choice & Entry Point (Lines 78-83)

```python
else:
    print("Invalid choice. Please select 1-5.")

if __name__ == "__main__":
    atm_simulation()
```

- **`else:`** handles any input that isn't 1-5
- **`if __name__ == "__main__":`** ensures the function only runs when the script is executed directly (not when imported as a module)

---

## 🎯 Program Flow Summary

```
Start
  ↓
Enter PIN (3 tries max)
  ↓
┌─────────────────────┐
│ ✅ PIN Correct?     │
│   Yes → Go to Menu  │
│   No → Try Again    │
│   3 Fails → Blocked │
└─────────────────────┘
  ↓
┌─────────────────────┐
│     ATM MENU        │
├─────────────────────┤
│ 1. Check Balance    │
│ 2. Deposit          │
│ 3. Withdraw         │
│ 4. Change PIN       │
│ 5. Exit → End       │
└─────────────────────┘
```

---

## 🔑 Key Python Concepts Used

1. **`while` loops** - For repeated PIN attempts and menu display
2. **`if/elif/else`** - For handling different menu choices
3. **`break`** - To exit loops
4. **`continue`** - To skip to next loop iteration
5. **`return`** - To exit the function early
6. **`f-strings`** - For formatted output (e.g., `f"Balance: ₹{balance:.2f}"`)
7. **String methods** - `.strip()`, `.isdigit()`, `.replace()`
8. **`__name__ == "__main__"`** - Standard Python entry point pattern
