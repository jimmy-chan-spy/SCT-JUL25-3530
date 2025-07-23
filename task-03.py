import string

def check_password_strength(password):
    length = len(password) >= 8
    uppercase = any(c.isupper() for c in password)
    lowercase = any(c.islower() for c in password)
    digit = any(c.isdigit() for c in password)
    special = any(c in string.punctuation for c in password)

    score = sum([length, uppercase, lowercase, digit, special])

    print("\nPassword Strength Report:")
    print("✔️ At least 8 characters" if length else "❌ Less than 8 characters")
    print("✔️ Contains uppercase letters" if uppercase else "❌ No uppercase letters")
    print("✔️ Contains lowercase letters" if lowercase else "❌ No lowercase letters")
    print("✔️ Contains numbers" if digit else "❌ No numbers")
    print("✔️ Contains special characters" if special else "❌ No special characters")

    # Overall rating
    if score == 5:
        return "🟢 Strong Password"
    elif 3 <= score < 5:
        return "🟡 Moderate Password"
    else:
        return "🔴 Weak Password"

# Example usage
password = input("Enter a password to test: ")
result = check_password_strength(password)
print("\nResult:", result)