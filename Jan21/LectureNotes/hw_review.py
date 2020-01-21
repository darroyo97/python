# LetterSummary


word = input("Enter a word >>")

empty_dic = {}

for letters in word:
    if letters not in empty_dic:
        empty_dic[letters] = 0
    empty_dic[letters] += 1
print(empty_dic)
