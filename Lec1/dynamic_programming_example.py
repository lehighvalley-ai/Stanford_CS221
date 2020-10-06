# SU CS221 Lecture 1
# Dyanmic Programming Example
# Find the minimum steps to change string s to match string t 
#    using substitution, deletion, and insertion 

def computed_distance(s, t):

    def recurse(m, n):
        '''
        Return the minimum edit distance between:
        - first m letters of s
        - first n letters of t
        '''
        if m == 0:
            result = n
        elif n == 0:
            result = m
        elif s[m - 1] == t[n - 1]: # Last letter matches
            result = recurse(m - 1, n - 1)
        else:
            sub_cost = 1 + recurse(m - 1, n - 1)
            del_cost = 1 + recurse(m - 1, n)
            ins_cost = 1 + recurse(m, n - 1)
            result = min(sub_cost, del_cost, ins_cost)
        return result
    
    return recurse(len(s), len(t))

# With memoization (known as tabling in logic programming)
def computed_distance_memoize(s, t):
    cache = {} # (m, n) => result
    def recurse(m, n):
        '''
        Return the minimum edit distance between:
        - first m letters of s
        - first n letters of t
        '''
        if (m, n) in cache:
            return cache[(m, n)]
        if m == 0: # base case
            result = n
        elif n == 0: # base case
            result = m
        elif s[m - 1] == t[n - 1]: # Last letter matches
            result = recurse(m - 1, n - 1)
        else:
            sub_cost = 1 + recurse(m - 1, n - 1)
            del_cost = 1 + recurse(m - 1, n)
            ins_cost = 1 + recurse(m, n - 1)
            result = min(sub_cost, del_cost, ins_cost)
        cache[(m, n)] = result
        return result
    
    return recurse(len(s), len(t))
    
if __name__ == "__main__":

    print(computed_distance("a cat", "the cats"))
    print(computed_distance_memoize("a cat" * 10, "the cats" * 10))
    