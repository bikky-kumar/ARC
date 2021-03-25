#!/usr/bin/python
#Bikky Kumars

import os, sys
import json
import numpy as np
import re

### Name: Bikky Kumar
### Student Id: 20235900
### url: https://github.com/bikky-kumar/ARC.git
### further details on tasks solved is also added on readme.md file


def solve_6d75e8bb(x):
    '''
        #comment-start
        Parameters:
        x (numpy array): a numpy array of M X N dimension, populated with values 0 and 8.
            [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 8, 8, 8, 0, 0, 0, 0, 0, 0],
            [0, 8, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 8, 8, 8, 8, 0, 0, 0, 0, 0],
            [0, 8, 8, 0, 0, 0, 0, 0, 0, 0],
            [0, 8, 8, 8, 0, 0, 0, 0, 0, 0],
            [0, 8, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 8, 8, 8, 0, 0, 0, 0, 0, 0],
            [0, 8, 8, 8, 0, 0, 0, 0, 0, 0],
            [0, 8, 8, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

      
          
        Returns:
            a numpy array (x) of M X N dimension with updated values to 2 by the pattern
            [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 8, 8, 8, 2, 0, 0, 0, 0, 0],
            [0, 8, 2, 2, 2, 0, 0, 0, 0, 0],
            [0, 8, 8, 8, 8, 0, 0, 0, 0, 0],
            [0, 8, 8, 2, 2, 0, 0, 0, 0, 0],
            [0, 8, 8, 8, 2, 0, 0, 0, 0, 0],
            [0, 8, 2, 2, 2, 0, 0, 0, 0, 0],
            [0, 8, 8, 8, 2, 0, 0, 0, 0, 0],
            [0, 8, 8, 8, 2, 0, 0, 0, 0, 0],
            [0, 8, 8, 2, 2, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        
        All the trainning and test grid are solved correctly. 
            
        # comment-end
    '''
    boundaries = np.where(x==8)
    ru = [(boundaries[0][i], boundaries[1][i]) for i in range(0, len(boundaries[0]))] 
   
   
    rows = [each[0] for each in ru]
    columns= [each[1] for each in ru]
    #column range to populate with 2
    col_range = min(columns), max(columns)
    #row range to populate with 2
    row_range = min(rows), max(rows)

    for i in range(row_range[0],row_range[1]+1):
        for j in range(col_range[0], col_range[1]+1):
            #check if it is already populated with 8
            if x[i][j] != 8:
                x[i][j] = 2
    
    return x



def solve_253bf280(x):
  
    '''  
        #comment-start
        Parameters:
        x (numpy array): a numpy array of M X N, populated with 0 and 8.
            [[0, 0, 0],
            [0, 8, 0],
            [0, 0, 0],
            [0, 8, 0]]
        
        
        Returns:
            a numpy array (x) of M X N dimension 
            [[0, 0, 0],
            [0, 8, 0],
            [0, 8, 0],
            [0, 8, 0]]
        
        All the trainning and test grid are solved correctly. 
        # comment-end 
    '''

    range_to_update = list()
    # The result is a tuple with first all the row indices, then all the column indices
    matching_index = np.where(x==8)
    # creating pairs of row column from matching_index
    ru = [(matching_index[0][i], matching_index[1][i]) for i in range(0, len(matching_index[0]))] 

    #finding range to update
    for i in range(0, len(ru)):
        r1, c1 = ru[i]
        for j in range(i+1, len(ru)):
            r2, c2 = ru[j]
            if r1 == r2 or c1 == c2:
                range_to_update.append([(r1, c1), (r2, c2)])
    

    # The loop updates values of numpy array x based on the range recorded.        
    for each in range_to_update:
        ll, ul = each
        if ll[0] == ul[0]:
            j = ll[1]+1
            while j < ul[1]:
                x[ll[0], j] = 3
                j +=1
        if ll[1] == ul[1]:
            i = ll[0]+1
            while i < ul[0]:
                x[i, ul[1]] = 3
                i += 1

    return x



def solve_3ac3eb23(x):
 
    '''        
        #comment-start
        Parameters:
        x (numpy array): a numpy array of M X N, populated with 0 and any value z on the 0th row of the array.
            [[0, 3, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
        
        
        Returns:
            a numpy array (x) of M X N dimension, with applied pattern 
            [[0, 3, 0],
            [3, 0, 3],
            [0, 3, 0],
            [3, 0, 3]]
            
        All the trainning and test grid are solved correctly. 
        # comment-end
    '''
    row, col = x.shape
    # holds, row_index, col_index, value
    pattern_on = [[ 0, i, x[0][i]] for i in range(0, col) if x[0][i] !=0] 
    
    #updates values for the numpy array x for each value recorded in pattern_on.
    for each in pattern_on:
        r, c, value = each
        i=r+1
        while(i<row):
            x[i][c-1] = value
            x[i][c+1] = value
            i = i+1
            if i< row:
                x[i][c] = value
                i = i+1
    return x

def main():
    # Find all the functions defined in this file whose names are
    # like solve_abcd1234(), and run them.

    # regex to match solve_* functions and extract task IDs
    p = r"solve_([a-f0-9]{8})" 
    tasks_solvers = []
    # globals() gives a dict containing all global names (variables
    # and functions), as name: value pairs.
    for name in globals(): 
        m = re.match(p, name)
        if m:
            # if the name fits the pattern eg solve_abcd1234
            ID = m.group(1) # just the task ID
            solve_fn = globals()[name] # the fn itself
            tasks_solvers.append((ID, solve_fn))
    print (tasks_solvers)

    for ID, solve_fn in tasks_solvers:
        # for each task, read the data and call test()
        directory = os.path.join("..", "data", "training")
        json_filename = os.path.join(directory, ID + ".json")
        data = read_ARC_JSON(json_filename)
        #send task_id, function_name, data loaded from json file
        test(ID, solve_fn, data)
    
def read_ARC_JSON(filepath):
    """Given a filepath, read in the ARC task data which is in JSON
    format. Extract the train/test input/output pairs of
    grids. Convert each grid to np.array and return train_input,
    train_output, test_input, test_output."""
    
    # Open the JSON file and load it 
    data = json.load(open(filepath))

    # Extract the train/test input/output grids. Each grid will be a
    # list of lists of ints. We convert to Numpy.
    train_input = [np.array(data['train'][i]['input']) for i in range(len(data['train']))]
    train_output = [np.array(data['train'][i]['output']) for i in range(len(data['train']))]
    test_input = [np.array(data['test'][i]['input']) for i in range(len(data['test']))]
    test_output = [np.array(data['test'][i]['output']) for i in range(len(data['test']))]

    return (train_input, train_output, test_input, test_output)


def test(taskID, solve, data):
    """Given a task ID, call the given solve() function on every
    example in the task data."""
    train_input, train_output, test_input, test_output = data
    print("Training grids")
    for x, y in zip(train_input, train_output):
        #print("input : \n", x)
        yhat = solve(x)
        #print("output: \n", yhat)
        show_result(x, y, yhat)
    print("Test grids")
    for x, y in zip(test_input, test_output):
        yhat = solve(x)
        show_result(x, y, yhat)

        
def show_result(x, y, yhat):
    print("Input")
    print(x)
    print("Correct output")
    print(y)
    print("Our output")
    print(yhat)
    print("Correct?")
    # if yhat has the right shape, then (y == yhat) is a bool array
    # and we test whether it is True everywhere. if yhat has the wrong
    # shape, then y == yhat is just a single bool.
    print(np.all(y == yhat))

if __name__ == "__main__": main()

