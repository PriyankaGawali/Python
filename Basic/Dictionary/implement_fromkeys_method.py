''' Implement fromKeys() method
 x = {1:2, 2:3, 3:4}
 possibility 1:[9]   then assign 9 to all keys
 possibility 2:[1,2,3] then 1 to 1 correspondence
 possibility 3:[7,8] then 1:7, 2:8, 3:None
 possibility 4:[7,8,9,10] then 1:7, 2:8 , 3:9 and 10 is skipped
'''

def assign_values(input_dict, values):
    result_dict = {}
    if type(values) == list or type(values) == tuple:
        keys_list = list(input_dict.keys())
        values_len = len(values)

        for i in range(len(keys_list)):
            if i < values_len:

                # handle 1 to 1 correspondence
                result_dict[keys_list[i]] = values[i]
            else:
                result_dict[keys_list[i]] = None

    else:
        result_dict = dict.fromkeys(input_dict, values)

    return result_dict


def main():
    dict_x = {1: 2, 2: 3, 3: 4}
    values = eval(input('Enter values : '))
    print("After assigning values : ", assign_values(dict_x, values))


if __name__ == '__main__':
    main()
