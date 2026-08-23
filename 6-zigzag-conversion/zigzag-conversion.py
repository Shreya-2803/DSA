class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or numRows>=len(s):
            return s
        rows=[""]*numRows
        curr_row=0
        down=True
        for char in s:
            rows[curr_row]+=char
            if curr_row==0:
                down=True
            elif curr_row==numRows-1:
                down=False
            if down:
                curr_row+=1
            else:
                curr_row-=1
        return "".join(rows)
