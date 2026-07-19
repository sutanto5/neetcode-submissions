from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        # compare windows
        window_len = len(s1)

        current_window = Counter(s2[:window_len])
        target = Counter(s1)

        if current_window == target:
            return True


        for i in range(window_len, len(s2)):

            # add right
            current_window[s2[i]] += 1

            # remove left
            removed_char = s2[i - window_len]
            current_window[removed_char] -= 1

            current_window = +current_window

            if current_window == target:
                return True
        
        return False
