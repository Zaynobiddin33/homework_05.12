### masala1  ########################################
# def check_words(str1: str, str2: str):
#     st1_list = str1.lower().split()
#     for i in st1_list:
#         if i not in str2.lower():
#             return False
#     return True

# print(check_words('Hello' , 'my name is that hello my dear'))



### masala2  ########################################
# def vowel(str1: str):
#     data = ['a','e','i','o','u']
#     count=0
#     for i in str1.lower():
#         if i in data:
#             count+=1
#     return count

# print(vowel('hello my friend how are you doin'))




### masala3  ########################################
# def zeros(*args):
#     count = 0
#     for i in args:
#         if i == 0:
#             count+=1
#     return count

# print(zeros(10,20,0,30,10,0,0))




### masala4  ########################################
# def vowel_in_str(str1: str, str2:str):
#     data = ['a','e','i','o','u']
#     we_have = []
#     for i in str1.lower():
#         if i in data:
#             we_have.append(i.lower())
#     for i in we_have:
#         if i not in str2.lower():
#             return False
#         return True

# print(vowel_in_str(' name', 'hi im good'))