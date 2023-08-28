class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        right_product = [1] * length
        left_product = [1] * length
        answer = [1] * length

        right = 1
        for i in range(length):
            right_product[i] = right
            right *= nums[i]
        
        left = 1
        for i in range(length - 1, -1, -1):
            left_product[i] = left
            left *= nums[i]

        for i in range(length):
            answer[i] = left_product[i] * right_product[i]

        return answer