class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result += num
        for number in nums:
            self.result += number
        print(f'Answer: {self.result}')
        return self

    def subtract(self, num, *nums):
        self.result -= num
        for number in nums:
            self.result -= number
        print(f'Answer: {self.result}')
        return self

# create an instance:
md = MathDojo()
# to test:
x = md.add(2).add(2, 5, 1).subtract(3,2).result
print(x)  
# should print 5
# run each of the methods a few more times and check the result!
# Write the add method and test it by calling it 3 times, with different numbers of arguments each time
# Write the subtract method and test it by calling it 3 times, with different numbers of arguments each time
prob1 = MathDojo()
y = prob1.add(100).add(-8, 20, 1).add(0).subtract(-87,250).result
print(y)  

prob2 = MathDojo()
z = prob2.add(77).add(10005, 852, 115).subtract(88, 98).subtract(568,1,-87).subtract(10381).result
print(z)  