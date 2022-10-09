class KMP:
    def __init__(self, needle, haystack):
        self.needle = needle
        self.haystack = haystack

    def generate_prefix_suffix_array(self):
        longest_prefix_suffix = [0]*len(self.needle)

        i = 0
        j = 1
        while j < len(self.needle):
            if self.needle[j] == self.needle[i]:
                longest_prefix_suffix[j] = i+1 # since everything is fine till i, so check from i+1
                i += 1
                j += 1
            elif i == 0:  # first character itself didn't match
                longest_prefix_suffix[j] = 0
                j += 1
            else:  # mismatch after atleast one matching character
                i = longest_prefix_suffix[i-1]  # don't increment j yet
        return longest_prefix_suffix

    def kmp(self):
        longest_prefix_suffix = self.generate_prefix_suffix_array()
        i, j, m, n = 0, 0, len(self.needle), len(self.haystack)

        while i < m and j < n:
            if self.needle[i] == self.haystack[j]:
                if i == m-1:
                    return True
                else:
                    i += 1
                    j += 1
            else:
                if i == 0:
                    j += 1
                else:
                    i = longest_prefix_suffix[i-1]
        return False

testcases = [["TEST","THIS IS A TEST TEXT"], ["AABA", "AABAACAADAABAABA"], ["AAAAB", "AAAAAAAAAAAAAAAAAB"], ["ABABAC", "ABABABCABABABCABABABC"]]
for testcase in testcases:
    solve = KMP(testcase[0], testcase[1])
    print(solve.kmp())

            


