letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[25::-1]
backwards2 = letters[::-1]
print(backwards)
print(backwards2)

print(letters[::-1][9:12]) # qpo
print(letters[::-1][-5:-1]) # edcb
print(letters[-8:][::-1]) # zyxwvuts "reversed last 8 character"
