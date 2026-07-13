class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
          # lett : freq
          s_map = {}
          # lett : freq
          t_map = {}

          for let in s:
               if let not in s_map:
                    s_map.update({let:1})
               else:
                    s_map[let] = s_map[let] + 1
                   
          
          for let in t:
               if let not in t_map:
                    t_map.update({let:1})
               else:
                    t_map[let] = t_map[let] + 1
          
          if t_map == s_map: 
               return True
          else:
               return False
