def is_increasing_list(some_list, k):
    
    if some_list[len(some_list) - 1] != k:
        return False
    if some_list[0] != 1:
        return False

    check = lambda a, b : b - a != 1 and b - a != 0

    #python version of for(int i = 0; i < some_list.size() - 1; i++)
    for i in range(len(some_list) - 1):
        if check(some_list[i], some_list[i + 1]) == True:
            return False
    return True

#python equivalent of C++ main() function
if __name__ == '__main__':
    some_list = [1, 2, 3, 4]
    print(is_increasing_list(some_list, 4))
    some_list = [1, 1, 2]
    print(is_increasing_list(some_list, 2))
    some_list = [1, 1, 3]
    print(is_increasing_list(some_list, 3))