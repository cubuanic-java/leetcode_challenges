class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Find a solution by going over all the numbers in the list
        For each number check if the compliment is in the remainder of the list
        
        Optimizations:
        
        First try: using a set, made it faster.
        
        Second try: using a dict instead of a list
        
        Third optimization, make it a one pass while creating the dict
        If the compliment is already in the dictionary we can return
        this is because there is only one solution
        
        """
        # create dictionary
        stored_numbers = {}
        for index, number in enumerate(nums):
            
            compliment = target - number
            
            # Two possibilities
            # 1.The compliment is already in the dict
            #   Return the answer
            # 2. Compliment is not in dict, store the number
            
            if compliment in stored_numbers:
                return [stored_numbers[compliment], index]
            
            stored_numbers[number] = index
            
        # this is an error!
        return -1