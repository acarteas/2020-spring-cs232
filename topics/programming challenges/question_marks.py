def replace_question_marks(some_string):
    for i in range(len(some_string)):

        before_char = '\0'
        after_char = '\0'
        if some_string[i] == '?':
            if i > 0:
                before_char = some_string[i - 1]
            if i < len(some_string) - 1:
                after_char = some_string[i + 1]
            new_char = (ord(before_char) + ord(after_char)) % 26
            new_char += ord('a')
            new_char = chr(new_char)
            some_string = some_string.replace("?", new_char, 1)
    return some_string

if __name__ == '__main__':
    print("?", replace_question_marks("?"))
    print("??", replace_question_marks("??"))
    print("???", replace_question_marks("???"))
    print("?a?", replace_question_marks("?a?"))
    print("a?a", replace_question_marks("a?a"))
    print("abc??cba?a", replace_question_marks("abc??cba?a"))
        