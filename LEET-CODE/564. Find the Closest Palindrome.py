class Solution:
    def nearestPalindromic(self, n: str) -> str:
        number = int(n)
        if number <= 10 :
            return str(number - 1)
        if number == 11 :
            return "9"

        length = len(n)
        leftHalf = int( n [ : (length + 1)  // 2 ] )

        def generatePalindrome( leftHalf , isEven ):
            palindrome=leftHalf
            if not isEven : 
                leftHalf//=10
            while leftHalf > 0 :
                palindrome = palindrome * 10 + leftHalf % 10
                leftHalf//=10
            return palindrome

        candidates = [0] * 5
        candidates[0] = generatePalindrome( leftHalf , length % 2 == 0 )
        candidates[1] = generatePalindrome( leftHalf - 1 , length % 2 == 0 )
        candidates[2] = generatePalindrome( leftHalf + 1 , length % 2 == 0 )
        candidates[3] = 10**(length-1) -1
        candidates[4] = 10**length + 1
        
        nearstPalindrome = 0
        minDifference = float("inf")
        for candidate in candidates:
            if candidate == number:
                continue
            diff = abs(candidate - number)
            if diff < minDifference or (diff == minDifference and candidate < nearestPalindrome):
                minDifference = diff
                nearestPalindrome = candidate
        return str(nearestPalindrome)