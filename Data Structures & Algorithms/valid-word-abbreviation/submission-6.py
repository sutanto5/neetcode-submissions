class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        
        ptr1 = 0
        ptr2 = 0

        while ptr1 < len(word) and ptr2 < len(abbr):
            if word[ptr1] == abbr[ptr2]:
                ptr1+=1
                ptr2+=1
            elif abbr[ptr2].isdigit():
                
                #get num
                num = ""

                while ptr2 < len(abbr) and abbr[ptr2].isdigit():
                    num+= abbr[ptr2]
                    ptr2+=1

                print(num)

                #invalid substring
                if num[0] == '0':
                    return False

                if int(num) > len(word):
                    return False
                
                # check in between
                ptr1 += int(num)
                

                # if ptr1 >= len(word) and ptr2 <= len(abbr):
                #     return False

                # print(word[ptr1])
                # print(abbr[ptr2])
                
                
                
            else:
                return False
        
        if ptr1 < len(word) or ptr2 < len(abbr):
            return False
        
        return True

