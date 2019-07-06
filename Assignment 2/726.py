import string
from collections import defaultdict

class Atom:
    def __init__(self, name, count):
        self.name = name
        self.count = int(count)
        self.mul = 1
        
    def __str__(self):
        return f"Atom {self.name} has {self.count}"
        
class Stack:
    def __init__(self):
        self.array = []
        
    def top(self):
        return "" if len(self.array) == 0 else self.array[-1]
    
    def push(self, char):
        self.array.append(char)
        
    def pop(self):
        return self.array.pop()
    
    def isEmpty(self):
        return len(self.array) == 0
    
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        lowercase = set(string.ascii_lowercase)
        uppercase = set(string.ascii_uppercase)
        level = 0
        numbers = set("1234567890")
        tokens = []
        atomNames = set()
        counter = defaultdict(int)
        postfix = []
        stack = Stack()
        index = 0
        currentToken = []
        end = len(formula) - 1
        while index < len(formula): # O(N)
            if formula[index] == "(" or formula[index] == ")":
                currentToken.append(formula[index])
            if formula[index] in uppercase:
                currentToken.append(formula[index])
                while index < end and formula[index + 1] in lowercase:
                    currentToken.append(formula[index + 1])
                    index += 1
                atomNames.add("".join(currentToken))
            if formula[index] in numbers:
                currentToken.append(formula[index])
                while index < end and formula[index + 1] in numbers:
                    currentToken.append(formula[index + 1])
                    index += 1
            index += 1
            tokens.append("".join(currentToken))
            currentToken = []
           
        for index, token in enumerate(tokens): # O(N)
            if token == "(":
                while stack.top() == "*":
                    postfix.append(stack.pop())
                if len(postfix) > 0 and tokens[index - 1] != "(":
                    stack.push("+")
                stack.push("(")
            elif token == ")":
                while stack.top() != "(":
                    postfix.append(stack.pop())
                stack.pop()
            elif str.isdigit(token):
                stack.push("*")
                postfix.append(token)
            else:
                while stack.top() == "*":
                    postfix.append(stack.pop())
                if len(postfix) > 0 and tokens[index - 1] != "(":
                    stack.push("+")
                postfix.append(token)
        
        while not stack.isEmpty():
            postfix.append(stack.pop())
        
        nestedList = []
        for i in range(len(postfix)): # O(N)
            token = postfix[i]
            if token == "+":
                right = stack.pop()
                left = stack.pop()
                temp = []
                if isinstance(left, str):
                    left = Atom(left, 1)
                if isinstance(left, Atom):
                    temp.append(left)
                if isinstance(right, str):
                    right = Atom(right, 1)
                if isinstance(right, Atom):
                    temp.append(right)
                if isinstance(left, list):
                    temp.extend(left)
                if isinstance(right, list):
                    temp.extend(right)
                stack.push(temp)
                
            elif token == "*":
                number = int(stack.pop())
                value = stack.pop()
                if isinstance(value, str):
                    stack.push(Atom(value, number))
                elif isinstance(value, Atom):
                    value.count *= number
                    stack.push(value)
                elif isinstance(value, list):
                    for atom in value:
                        atom.mul *= int(number)
                    stack.push(value)
                else:
                    print("Should not happen!")
            else:
                stack.push(token)
        
        atomList = stack.pop()
        if isinstance(atomList, list):
            for atom in atomList:
                counter[atom.name] += atom.count * atom.mul
            sortedName = sorted(counter.keys())
            result = []
            for key in sortedName:
                if counter[key] == 1:
                    result.append(f"{key}")
                else:
                    result.append(f"{key}{counter[key]}")
            return "".join(result)
        elif isinstance(atomList, str):
            return atomList
        else:
            if atomList.count == 1:
                return f"{atomList.name}"
            else:
                return f"{atomList.name}{atomList.count}"
            
# O(N) for time and space
