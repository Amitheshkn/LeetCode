class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        columns = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for each_row_index in range(9):
            for each_column_index in range(9):
                if board[each_row_index][each_column_index] == ".":
                    continue

                if (board[each_row_index][each_column_index] in rows[each_row_index] or 
                    board[each_row_index][each_column_index] in columns[each_column_index] or 
                    board[each_row_index][each_column_index] in squares[(each_row_index // 3, each_column_index // 3)]):
                    return False

                rows[each_row_index].add(board[each_row_index][each_column_index])
                columns[each_column_index].add(board[each_row_index][each_column_index])
                squares[(each_row_index // 3,each_column_index // 3)].add(board[each_row_index][each_column_index])    

        return True
