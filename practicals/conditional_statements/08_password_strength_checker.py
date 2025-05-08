# Q: Check if password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium) and >10 chars (Strong)

password = str(input("Enter the password to check: "))

chars = len(password)

if chars < 6:
    strength = "Weak"
elif chars <= 10:
    strength = "Medium"
else:
    strength = "Strong"

print("Your password strength is", strength)
