class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        rows = [""]* numRows
        current = 0
        dir = 1
        print(s, numRows)
        
        for i in s:
            print("iii",i, "curr:",current, "dir", dir)
            rows[current] += i
            if current == 0 and numRows == 1:
                dir = 0
            elif current == 0:
                dir = 1
            elif current == (numRows-1):
                print("ivde")
                dir = -1
            
            current += dir
        return "".join(rows)
        
        
        
        