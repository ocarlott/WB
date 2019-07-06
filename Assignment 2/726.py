import string
from collections import defaultdict

class Atom:
    def __init__(self, name = None):
        self.name = name
        self.count = 1
        
    def addName(self, name):
        self.name = name
        
    def addCount(self, stCount):
        self.count = int(stCount)
        
    def __str__(self):
        return f"Atom {self.name} has {self.count}"
        
class ListNode:
    def __init__(self, level):
        self.atoms = []
        self.level = level
        self.mul = 1
        
    def addMul(self, mul):
        self.mul *= int(mul)
        
    def __repr__(self):
        print(f"There are {len(self.atoms)} atoms and mul of {self.mul}:")
        for atom in self.atoms:
            print(atom)
        return ""
        
class KeyNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None
        
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        lowercase = set(string.ascii_lowercase)
        uppercase = set(string.ascii_uppercase)
        level = 0
        currentAtoms = None
        currentName = []
        currentCount = []
        currentMul = []
        listCounter = []
        keyRoot = None
        startMul = False
        
        def propagrateMul(mul, level):
            for ln in listCounter:
                if ln.level > level:
                    ln.mul *= int(mul)
                    ln.level -= 1
        
        def addToKeyTree(el):
            nonlocal keyRoot
            if keyRoot is None:
                keyRoot = KeyNode(el)
            else:
                current = keyRoot
                while True:
                    if current.name > el:
                        if current.left is None:
                            current.left = KeyNode(el)
                            break
                        else:
                            current = current.left
                    elif current.name < el:
                        if current.right is None:
                            current.right = KeyNode(el)
                            break
                        else:
                            current = current.right
                    else:
                        break
                        
        for i in range(len(formula)):
            if formula[i] in lowercase:
                # Only capital char (in the same atom) can be in front of this letter
                currentName.append(formula[i])
            elif formula[i] in uppercase:
                # What can be in front of this char are: Atom count, Atom name, Multiplier, ( and Nothing
                if len(currentName) > 0:
                    name = "".join(currentName)
                    addToKeyTree(name)
                    currentAtoms = currentAtoms if not currentAtoms is None else ListNode(level)
                    currentAtoms.atoms.append(Atom(name))
                    currentName = []
                if len(currentCount) > 0:
                    currentAtoms.atoms[-1].addCount("".join(currentCount))
                    currentCount = []
                if len(currentMul) > 0:
                    mul = "".join(currentMul)
                    currentAtoms.addMul(mul)
                    propagrateMul(mul, level)
                    level -= 1
                    startMul = False
                    currentMul = []
                    listCounter.append(currentAtoms)
                    currentAtoms = ListNode(level)
                currentName.append(formula[i])
            elif formula[i] == "(":
                # What can be in front of this char are: Atom name, Atom count, and Multiplier
                level += 1
                if len(currentName) > 0:
                    name = "".join(currentName)
                    addToKeyTree(name)
                    currentAtoms = currentAtoms if not currentAtoms is None else ListNode(level)
                    currentAtoms.atoms.append(Atom(name))
                    currentName = []
                if len(currentCount) > 0:
                    currentAtoms.atoms[-1].addCount("".join(currentCount))
                    currentCount = []
                if len(currentMul) > 0:
                    mul = "".join(currentMul)
                    currentAtoms.addMul(mul)
                    propagrateMul(mul, level)
                    level -= 1
                    startMul = False
                    currentMul = []
                if not currentAtoms is None and len(currentAtoms.atoms) > 0:
                    listCounter.append(currentAtoms)
                    currentAtoms = ListNode(level)
            elif formula[i] == ")":
                # What can be in front of this char are: Atom count, Atom name and Multiplier
                if len(currentName) > 0:
                    name = "".join(currentName)
                    addToKeyTree(name)
                    currentAtoms = currentAtoms if not currentAtoms is None else ListNode(level)
                    currentAtoms.atoms.append(Atom(name))
                    currentName = []
                if len(currentCount) > 0:
                    currentAtoms.atoms[-1].addCount("".join(currentCount))
                    currentCount = []
                if len(currentMul) > 0:
                    mul = "".join(currentMul)
                    currentAtoms.addMul(mul)
                    propagrateMul(mul, level)
                    level -= 1
                    startMul = False
                    currentMul = []
                startMul = True
            else: # Number
                if startMul:
                    currentMul.append(formula[i])
                else:
                    currentCount.append(formula[i])
            
            if i == len(formula) - 1:
                # These can be at the end of string: Atom name, Atom count and Multiplier
                if len(currentName) > 0:
                    name = "".join(currentName)
                    addToKeyTree(name)
                    currentAtoms.append(Atom(name))
                    currentName = []
                if len(currentCount) > 0:
                    currentAtoms.atoms[-1].addCount("".join(currentCount))
                    currentCount = []
                if len(currentMul) > 0:
                    mul = "".join(currentMul)
                    level -= 1
                    if len(currentAtoms.atoms) > 0:
                        currentAtoms.addMul(mul)
                    propagrateMul(mul, level)
                    startMul = False
                    currentMul = []
                if len(currentAtoms.atoms) > 0:
                    listCounter.append(currentAtoms)
          
        counter = defaultdict(int)
        result = []
        # for ln in listCounter:
        #     print(ln)
        for ln in listCounter:
            for atom in ln.atoms:
                counter[atom.name] += atom.count * ln.mul
                
        def traverseKeyTree(rt):
            if not rt.left is None:
                traverseKeyTree(rt.left)
            if counter[rt.name] == 1:
                result.append(rt.name)
            else:
                result.append(f"{rt.name}{counter[rt.name]}")
            if not rt.right is None:
                traverseKeyTree(rt.right)
                
        traverseKeyTree(keyRoot)
        return "".join(result)
