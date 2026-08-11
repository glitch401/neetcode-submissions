class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # res = ""
        # z_s = zip(*strs)
        # for z in z_s:
        #     c = set(z)
        #     if len(c)==1:
        #         res+=next(iter(c))
        #     else:
        #         break
        # return res

        if not strs:
            return ""
        
        #build trie
        root = TrieNode()
        for word in strs:
            if not word:
                return ""
            
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_end=True
        
        #treverse down
        prefix = []
        node = root

        while len(node.children)==1 and not node.is_end:
            char, next_node = next(iter(node.children.items()))
            prefix.append(char)
            node = next_node
        
        return "".join(prefix)
