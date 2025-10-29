from homework_5.tracer import tracer

def permutations(nums):
    result = []
    @tracer
    def backtrack(start=0):
        if start == len(nums):
            result.append(nums[:])
            return
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]  
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]

    backtrack()
    return result

