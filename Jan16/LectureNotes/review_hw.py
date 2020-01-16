# dim1 = [[2, -2], [5, 3]]
# dim2 = [[2, -2], [5, 3]]
# result_list = []
# for index1 in range(len(dim1)):
#     for index2 in range(len(dim2)):
#         if index1 == index2:
#             working_list = []
#             sum1 = dim1[index1][0] + dim2[index2][0]
#             sum2 = dim1[index1][1] + dim2[index2][1]
#             working_list.append(sum1)
#             working_list.append(sum2)
#             result_list.append(working_list)
# print(result_list)


# http://www.pythontutor.com/live.html#mode=edit
# To see step by step

# a = [[2, -2], [5, 3]]
# b = [[2, -2], [5, 3]]
# result = [[0, 0], [0, 0]]
# for i in range(len(a)):
#     for j in range(len(a[0])):
#         result[i][j] = a[i][j] + b[i][j]
# for r in result:
#     print(r)

# de-dup
# a = [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 9, 10, 10]
# b = a.copy()
# b = list(set(a))
# print(b)

# de-up for statement

# original = [1, 2, 2, 3, 1]
# newlist = []
# for item in original:
#     if item in newlist:
#         print("You don't need to add "+str(item)+" again.")
#     else:
#         newlist.append(item)
#         print("Added "+str(item))
# print(newlist)

# leetspeak


# normal_sentence = "I am a leet programmer".upper()
# leet_list = list(normal_sentence)
# for i in range(len(leet_list)):
#     if leet_list[i] == 'A':
#         leet_list[i] = '4'
#     elif leet_list[i] == 'E':
#         leet_list[i] = '3'
#     elif leet_list[i] == 'G':
#         leet_list[i] = '6'
#     elif leet_list[i] == 'I':
#         leet_list[i] = '1'
#     elif leet_list[i] == 'O':
#         leet_list[i] = '0'
#     elif leet_list[i] == 'S':
#         leet_list[i] = '5'
#     elif leet_list[i] == 'T':
#         leet_list[i] = '7'
# leet_sentence = "".join(leet_list)
# print(leet_sentence.lower())


# leet = {'A': '4','E': '3','G': '6','I': '1','O': '0','T': '7','S': '5'}
# para = ("I pledge allegiance to the Flag of the United States of America, and to the Republic for which it stands, one Nation under God, indivisible, with liberty and justice for all.")
# para = para.upper()
# for i, j in leet.items():
#     para = para.replace(i, j)
# print (para)


# shakespeare = """All that glitters is not gold
# Fair is foul, and foul is fair: Hover through the fog and filthy air.""""
# shake_upper = shakespeare.upper()
# shake_list = list(shake_upper)
# leet_shake = []
# leet = {"A": "4", "E": "3", "G": "6", "I": "1", "O": "0", "S": "5", "T": "7"}
# for letter in shake_upper:
#     if letter in leet:
#         letter = leet[letter]
#         leet_shake.append(letter)
#     else:
#         leet_shake.append(letter)
# final = "".join(leet_shake).lower()
# print(final)

# 6 solution:
# string_to_vowel_check = 'Good'
# last_letter = ''
# new_string = ''
# for letter in string_to_vowel_check:
#     is_vowel = False
#     if letter == last_letter:
#         if letter == 'a' or letter == 'A':
#             is_vowel = True
#         elif letter == 'e' or letter == 'E':
#             is_vowel = True
#         elif letter == 'i' or letter == 'I':
#             is_vowel = True
#         elif letter == 'o' or letter == 'O':
#             is_vowel = True
#         elif letter == 'u' or letter == 'U':
#             is_vowel = True
#     last_letter = letter
#     if is_vowel == True:
#         letter = letter*4
#     new_string += letter
# print(new_string)


# 7. caesar chiper
# txt = "lbh zhfg hayrnea jung lbh unir yrnearq"  # message
# alpha = "abcdefghijklmnopqrstuvwxyz"
# offset = int(input("Please input offset number  "))
# result = ""
# for char in txt:
#     # print(type(alpha.find(char)))
#     if char in alpha:
#         alpha_index = (alpha.find(char)-offset) % len(alpha)
#         result = result + alpha[alpha_index]
#     else:
#         result = result + char
# print(result)

# vowels = (('aa', 'aaaaa'), ('ee', 'eeeee'), ('oo', 'ooooo'), ('ii', 'iiiii'), ('uu', 'uuuuu'))
# text = input("Enter a word with duplicate vowels in it .. (Good) ")
# vow_text = text
# for old, new in vowels:
#     vow_text = vow_text.replace(old, new)
# print (vow_text)
