class Trie:
    def __init__(self):
        self.root = {}
        self.end = '*'
    
    def insert(self, word):
        cur = self.root
        for c in word:
            if c in cur:
                cur = cur[c]
            else:
                cur[c] = {}
                cur = cur[c]
        cur[self.end] = True
        
    def count_wildcard(self, wc):
        cur = self.root
        to_process = [cur]
        for c in wc:
            if not to_process:
                return 0
            if c == '?':
                process_next = []
                while to_process:
                    cur = to_process.pop()
                    for k in cur:
                        if k != self.end:
                            process_next.append(cur[k])
                to_process = process_next
                
            else:
                process_next = []
                while to_process:
                    cur = to_process.pop()
                    if c in cur:
                        process_next.append(cur[c])
                to_process = process_next
        count = 0
        for tp in to_process:
            if self.end in tp:
                count += 1
        return count

# for each query find number of words which match that pattern. "?" is wildcard character.                
input_strings = ["Cat", "Bat", "Pat", "Man", "Jam", "Jan"]
queries = ["?at", "?a?", "J??"]

tr = Trie()
for ip in input_strings:
    tr.insert(ip)

for q in queries:
    print(tr.count_wildcard(q))
