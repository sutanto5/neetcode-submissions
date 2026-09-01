class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for word in strs:
            encoded_string = encoded_string + word + "\n"

        return encoded_string

    def decode(self, s: str) -> List[str]:
        strs = s.split("\n")
        return strs[0:len(strs)-1]
