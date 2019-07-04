from collections import defaultdict

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        # Make a counter dictionary
        # Loop through list
            # Slice with space to get count and domain
            # Break domain down into each word
            # Make different combinations out of each word
            # Add the domains with count into dictionary
        # Construct a list of string from counter dictionary
        counter = defaultdict(int) # O(N)
        result = [] # O(N)
        for s in cpdomains: # O(N)
            s = s.split(" ") # O(M)
            count = int(s[0])
            domainKeys = s[1].split(".") # O(M)
            length = len(domainKeys)
            for i in range(length): # O(1) since each address will have either 1 or 2 dots
                domain = ".".join(domainKeys[i:length]) # O(M)
                counter[domain] += count
        for key, value in counter.items(): # O(N)
            result.append(f"{value} {key}")
        return result

# O(NM) for time. O(N) for space.
