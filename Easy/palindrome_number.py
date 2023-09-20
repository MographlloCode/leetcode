"""

  Given an integer x, return true if x is a 
  palindrome
  , and false otherwise.

  

  Example 1:

  Input: x = 121
  Output: true
  Explanation: 121 reads as 121 from left to right and from right to left.
  Example 2:

  Input: x = -121
  Output: false
  Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
  Example 3:

  Input: x = 10
  Output: false
  Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
  

  Constraints:

  -231 <= x <= 231 - 1
  

  Follow up: Could you solve it without converting the integer to a string?

"""

class MySolution:
    ''' This is my solution after watching some videos and understanding the math behind it '''
    def isPalindrome(self, x: int) -> bool:
        ''' 

          Execution Time: 44ms → Beats 97.94%of users with Python3
          Memory: 16.16mb → Beats 92.38%of users with Python3

          ## This is the logic at this solution:
         
          We first look to use the fail first method, checking if the number is negative or if it ends with zero, numbers that ends with zero can't be palindrome because they would need to start with zero, and this just doesn't exists.

          After that we declare a variable to store half of the number that we will input
          - `num_half = 0`

          Then we iterate compairing the input to the half, while the input is greater than the half, it keeps going

          Inside the loop we will do some math operations, first we are going to update the half_num with the last number of the integer, multipling the half num by 10 and adding it to the module of our number to 10, like this;

          `num_half = (num_half * 10) + (x % 10)`
          
          Then we will use the floor division (Dividing a number and rounding it down) to update our input

          `x = x // 10`

          The loop will continue 'till the num_half be greater than the input, and at this point we will return True or False, depending on 2 factors.

          If the input(x) is equal to the num_half, the return is True, but this will only works with numbers that has a even ammount of digits

          to check and odd digits number we must do another verification that consists in compairing the input(x) with the floor division of our half to 10, like this:

          `return(x == num_half or x == num_half // 10)`

          If the numbers match, than it will return True, otherwise, will return False.

          That's it folks!

        '''

        if x < 0 or (x != 0 and x % 10 == 0):
            return(False)
        
        num_half = 0

        while x > num_half:
            num_half = (num_half * 10) + (x % 10)
            x = x // 10

        return(x == num_half or x == num_half // 10)
    
class UpvoteSolution:
    ''' This is the most liked solution on leetcode for this problem '''
    def isPalindromeSolutionOne(self, x: int) -> bool:
        ''' 
          Solution 1:
            Execution Time: 73ms → Beats 21.05%of users with Python3
            Memory: 16.29mb → Beats 67.55% of users with Python3

          Suggestions to make them better are always welcomed.

          #### Solution 1:
            This is the easiest way to check if integer is palindrome.

            Convert the number to string and compare it with the reversed string.

            I wrote this working solution first and then found in the description that we need to solve this problem without converting the input to string. Then I wrote solution 2.

            def isPalindrome(self, x: int) -> bool:
              if x < 0:
                return False
              
              return str(x) == str(x)[::-1]

            If we don't want to convert the number to string, then recreate a new number in reverse order.

        '''

        if x<0:
          return False

        inputNum = x
        newNum = 0
        while x>0:
          newNum = newNum * 10 + x%10
          x = x//10
        return newNum == inputNum
    
    def isPalindromeSolutionOne(self, x: int) -> bool:
        ''' 

          Execution Time: 67ms → Beats 38.02%of users with Python3
          Memory: 16.12mb → Beats 92.38% of users with Python3

          #### Solution 2:
            I'd recommend you to solve leetcode question 7 (reverse integer) to understand the logic behind this solution.

            Python3 int type has no lower or upper bounds. But if there are constraints given then we have to make sure that while reversing the integer we don't cross those constraints.

            So, instead of reversing the whole integer, let's convert half of the integer and then check if it's palindrome.
            But we don't know when is that half going to come.

            Example, if x = 15951, then let's create reverse of x in loop. Initially, x = 15951, revX = 0

            x = 1595, revX = 1
            x = 159, revX = 15
            x = 15, revX = 159
            We see that revX > x after 3 loops and we crossed the half way in the integer bcoz it's an odd length integer.
            If it's an even length integer, our loop stops exactly in the middle.

            Now we can compare x and revX, if even length, or x and revX//10 if odd length and return True if they match.

            There's a difference between / and // division in Python3.

        '''

        if x < 0 or (x > 0 and x % 10 == 0):   # if x is negative, return False. if x is positive and last digit is 0, that also cannot form a palindrome, return False.
              return False
            
              result = 0
              
              while x > result:
                result = result * 10 + x % 10
                x = x // 10
                
              return True if (x == result or x == result // 10) else False