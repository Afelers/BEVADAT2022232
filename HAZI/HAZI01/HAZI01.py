# %%
# Create a function that returns with a subsest of a list.
# The subset's starting and ending indexes should be set as input parameters (the list aswell).
# return type: list
# function name must be: subset
# input parameters: input_list,start_index,end_index

# %%
# 1
def subset(input_list, start_index, end_index):
    output_list = []
    for i in range(end_index - start_index):
        output_list.append(input_list[start_index + i])
    return output_list

# %%
# Create a function that returns every nth element of a list.
# return type: list
# function name must be: every_nth
# input parameters: input_list,step_size

# %%
# 2
def every_nth(input_list, step_size):
    output_list = []
    for i in range(0, len(input_list), step_size):      # start index should most definitely be step_size - 1 but who knows at this point
        output_list.append(input_list[i])
    return output_list

# %%
# Create a function that can decide whether a list contains unique values or not
# return type: bool
# function name must be: unique
# input parameters: input_list

# %%
# 3
def unique(input_list):
    temp = []
    for item in input_list:
        if item in temp:
            return False
        else:
            temp.append(item)
    return True

# %%
# Create a function that can flatten a nested list ([[..],[..],..])
# return type: list
# function name must be: flatten
# input parameters: input_list

# %%
# 4
def flatten(input_list):
    return [item for inner in input_list for item in inner]

# %%
# Create a function that concatenates n lists
# return type: list
# function name must be: merge_lists
# input parameters: *args


# %%
# 5
def merge_lists(*args):
    output_list = []
    for arg in args:
        output_list.append(arg)
    return flatten(output_list)

# %%
# Create a function that can reverse a list of tuples
# example [(1,2),...] => [(2,1),...]
# return type: list
# fucntion name must be: reverse_tuples
# input parameters: input_list

# %%
# 6
def reverse_tuples(input_list):
    for i in range(len(input_list)):
        input_list[i] = list(input_list[i])
        input_list[i].reverse()
        input_list[i] = tuple(input_list[i])
    return input_list

# %%
# Create a function that removes duplicates from a list
# return type: list
# function name must be: remove_tuplicates
# input parameters: input_list

# %%
# 7
def remove_duplicates(input_list):
    output_list = []
    for item in input_list:
        if item not in output_list:
            output_list.append(item)
    return output_list

# just to be sure in case the aforementioned func name does not actually have a typo
def remove_tuplicates(input_list):
    output_list = []
    for item in input_list:
        if item not in output_list:
            output_list.append(item)
    return output_list

# %%
# Create a function that transposes a nested list (matrix)
# return type: list
# function name must be: transpose
# input parameters: input_list

# %%
# 8
def transpose(input_list):
    transposed_matrix = []
    for i in input_list[0]:
        transposed_matrix.append([])

    for i in range(len(input_list)):
        for j in range(len(input_list[i])):
            transposed_matrix[j].append(input_list[i][j])
    return transposed_matrix

# %%
# Create a function that can split a nested list into chunks
# chunk size is given by parameter
# return type: list
# function name must be: split_into_chunks
# input parameters: input_list,chunk_size

# %%
# 9     
import math
def split_into_chunks(input_list, chunk_size):
    output_list = []
    #input_list = flatten(input_list)                           # gonna check without this line, either your test is wrong or the task is misspelled as it says input_list IS a nested list
    for i in range(math.ceil(len(input_list) / chunk_size)):
        output_list.append([])

    idx = -1
    for i in range(len(input_list)):
        if i % chunk_size == 0:
            idx += 1
        output_list[idx].append(input_list[i])
    return output_list

# %%
# Create a function that can merge n dictionaries
# return type: dictionary
# function name must be: merge_dicts
# input parameters: *dict

# %%
# 10
def merge_dicts(*dict):
    merged_dicts = {}
    for d in dict:
        merged_dicts.update(d)
    return merged_dicts

# %%
# Create a function that receives a list of integers and sort them by parity
# and returns with a dictionary like this: {"even":[...],"odd":[...]}
# return type: dict
# function name must be: by_parity
# input parameters: input_list

# %%
# 11
def by_parity(input_list):
    output_dict = { "even" : [], "odd" : [] }
    for item in input_list:
        if item % 2 == 0:
            output_dict["even"].append(item)
        else:
            output_dict["odd"].append(item)
    return output_dict

# %%
# Create a function that receives a dictionary like this: {"some_key":[1,2,3,4],"another_key":[1,2,3,4],....}
# and return a dictionary like this : {"some_key":mean_of_values,"another_key":mean_of_values,....}
# in short calculates the mean of the values key wise
# return type: dict
# function name must be: mean_key_value
# input parameters: input_dict

# %%
# 12
def mean_key_value(input_dict):
    for key, value in input_dict.items():
        input_dict[key] = sum(value) / len(value)
    return input_dict

# %%
# If all the functions are created convert this notebook into a .py file and push to your repo


