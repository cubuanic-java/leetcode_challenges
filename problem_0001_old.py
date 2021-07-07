test_list = [2, 5, 7, 9, 3, 1]
print(test_list)

dict_numbers = {}
for index, number in enumerate(test_list):

    if number not in dict_numbers:
        dict_numbers[number] = [index]
    else:
        dict_numbers[number].append(index)

def solution(target):

    for number in dict_numbers:

        # NB, key = the number, the val is the index!

        compliment = target - number

        if compliment in dict_numbers:
            # if compliment equals target, it needs to exist twice!
            if (compliment == number):
                if len(dict_numbers[compliment]) == 1:
                    pass
                else:
                    return dict_numbers[number]
            else:
                index_1 = dict_numbers[number][0]
                index_2 = dict_numbers[compliment][0]
            
            return [index_1, index_2]

sol = solution(6)
print(sol)

# def twoSum(self, nums, target):
#         seen = {}
#         for i, v in enumerate(nums):
#             remaining = target - v
#             if remaining in seen:
#                 return [seen[remaining], i]
#             seen[v] = i
#         return []