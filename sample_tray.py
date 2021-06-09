def getAdjacentPositiveSamples(rows: int,cols: int,entries: list):
    '''
    Returns a dictionary with keys corresponding each row and values corresponding to the adjacent covid positive samples
    '''

    # Check inputs
    if not (isinstance(rows,int) and isinstance(cols,int) and isinstance(entries,list)):
        print("Invalid input")
        return {}

    # converts array into matrix
    import numpy as np
    matrix = np.array(entries).reshape(rows, cols)
    output_dict = {}

    # for each element in the matrix, do
    for row in range(rows):
        row_list = []
        recorder = False
        adjacent_list = []
        for col in range(cols):
            current_cell = matrix[row][col]
            next_cell = matrix[row][col+1] if col+1 < cols else None

            # Turns the recorder ON
            if current_cell == 1 and next_cell == 1:
                recorder = True

            # checks if the recorder is ON. Then appends index value of the current cell into a temporary list
            if recorder:
                adjacent_list.append(col)

            # Turns the recorder OFF and reset the list
            if current_cell == 1 and next_cell == 0:
                recorder = False
                adjacent_list = []
            
            # Removes duplicate and null lists appends to the parent row_list
            if adjacent_list not in row_list and adjacent_list != []:
                row_list.append(adjacent_list)
            
        # appends temp_list into output_dict
        output_dict[row] = row_list

    return output_dict

if __name__ == "__main__":
    # user inputs
    rows = int(input("Enter the number of rows:"))
    cols = int(input("Enter the number of columns:"))
    entries = list(map(int, input("Enter the entries in a single line (separated by space):\n").split()))

    # # test inputs 1
    # rows1 = 3
    # cols1 = 8
    # seq1 = "1 0 1 1 0 1 1 1 0 1 1 0 0 1 1 0 1 1 0 0 1 1 1 0".split(' ')
    # entries1 = list(map(int, seq1))

    # # test inputs 2
    # rows2 = 5
    # cols2 = 5
    # seq2 = '0 1 1 1 1 1 0 0 1 1 0 0 0 0 1 1 0 1 0 1 0 1 1 0 0'.split(' ')
    # entries2 = list(map(int, seq2))

    data = getAdjacentPositiveSamples(rows,cols,entries)

    # Prints the calculate value in the preferred form
    for key,value in data.items():
        row = f'Row {key+1}:'
        col = ''
        for i in value:
            temp_string = ''
            for j in i:
                temp_string += f'Col-{j},'
            col += f"{len(i)}" + f"[{temp_string}]; "

        print(row,col)