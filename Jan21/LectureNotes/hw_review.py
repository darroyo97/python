# # LetterSummary


# word = input("Enter a word >>")

# empty_dic = {}

# for letters in word:
#     if letters not in empty_dic:
#         empty_dic[letters] = 0
#     empty_dic[letters] += 1
# print(empty_dic)

# word summary
# 2.
sent_histogram = {}
entered_sentence = input("Please enter a sentence... ")
sent_to_words = entered_sentence.split()
for repeats in sent_to_words:
    if repeats not in sent_histogram:
        sent_histogram[repeats] = 0
    sent_histogram[repeats] += 1
print(sent_histogram)
