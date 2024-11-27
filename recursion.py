#Sum of N natural numbers

class Solution:
    def calculateSum(self, N):
        if N == 1:
            return 1
        else:
            return N + self.calculateSum(N-1)
    



# Recursion Design Gurus

def printNumbers(n):
    if n < 0:
        return
    
    printNumbers(n-1)
    print(n)
    

printNumbers(5)

'''

during the unwinding process lets look at the function call printNumbers(0). How does it know that from the program 
def printNumbers(n):
    if n < 0:
        return
    
    printNumbers(n-1)
    print(n)
    
it only needs to execute print(0) and ignore the lines     if n < 0:
        return
    
    printNumbers(n-1)?
        This is an excellent question about how program execution maintains its position during recursion.
Call Stack Memory
When printNumbers(0) is executing, it maintains its own execution pointer that keeps track of which line of code it's currently executing. Here's the detailed breakdown:
python
def printNumbers(n):   # Line 1
    if n < 0:         # Line 2
        return        # Line 3
    
    printNumbers(n-1) # Line 4
    print(n)         # Line 5

For printNumbers(0), the execution flow is:
Initially executes Line 2: checks if 0 < 0 (false)
Moves to Line 4: calls printNumbers(-1)
The execution pointer for printNumbers(0) stays at Line 4 while printNumbers(-1) executes
When printNumbers(-1) returns, the pointer moves to Line 5
Executes print(0)
Stack Frame
Each function call creates a stack frame containing:
The current value of n (0 in this case)
The return address (where to continue after the function completes)
The current execution pointer (which line to execute next)
When printNumbers(-1) returns, the program:
Pops printNumbers(-1)'s stack frame
Returns to printNumbers(0)'s stack frame
Continues from where it left off (Line 4)
Moves to the next instruction (Line 5)
Memory Visualization
text
Stack Frame for printNumbers(0):
{
    n: 0
    execution_pointer: Line 4 → Line 5
    local_variables: {}
}

The program doesn't need to re-execute the previous lines because the execution pointer remembers exactly where it left off in each stack frame. 
This is a fundamental feature of how function calls work in programming languages, whether recursive or not.
    '''
    
#factorial

def factorial(n):
    if n == 1 or n == O:
        return 1
    return n * factorial(n-1)
    
    
        
        