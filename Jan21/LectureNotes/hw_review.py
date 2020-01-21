# LetterSummary


# word = input("Enter a word >>")

# empty_dic = {}

# for letters in word:
#     if letters not in empty_dic:
#         empty_dic[letters] = 0
#     empty_dic[letters] += 1
# print(empty_dic)

# word summary
# 2.
# sent_histogram = {}
# entered_sentence = input("Please enter a sentence... ")
# sent_to_words = entered_sentence.split()
# for repeats in sent_to_words:
#     if repeats not in sent_histogram:
#         sent_histogram[repeats] = 0
#     sent_histogram[repeats] += 1
# print(sent_histogram)
# 3 sorting histogram
LC = {}

word = input("Please enter a word to count top 3 letters: ")
# word=‘hellllooooooohahahhhhh’
for l in word:
    if l in LC:
        LC[l] = LC[l]+1
    else:
        LC[l] = 1
top_list = [["", 0], ["", 0], ["", 0]]
for k, v in LC.items():
    if v > top_list[0][1]:
        top_list[2][0] = top_list[1][0]
        top_list[2][1] = top_list[1][1]
        top_list[1][0] = top_list[0][0]
        top_list[1][1] = top_list[0][1]
        top_list[0][0] = k
        top_list[0][1] = v
    elif v > top_list[1][1]:
        top_list[2][0] = top_list[1][0]
        top_list[2][1] = top_list[1][1]
        top_list[1][0] = k
        top_list[1][1] = v
    elif v > top_list[2][1]:
        top_list[2][0] = k
        top_list[2][1] = v
print(top_list)
