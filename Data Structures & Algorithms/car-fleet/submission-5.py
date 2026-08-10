class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p,s] for p,s in zip(position, speed)]
        pair = sorted(pair, key=lambda x: x[0], reverse=True)
        stack = []
        for p,s in pair:
            t = (target-p)/s
            if not stack or stack[-1]<t:
                stack.append(t)
        return len(stack)