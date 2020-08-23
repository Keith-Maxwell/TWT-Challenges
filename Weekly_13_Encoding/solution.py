def solution(text):
    word_list = text.split()
    word_count_dict = {word: word_list.count(word) for word in word_list}
    word_sorted = [k for k, v in sorted(word_count_dict.items(), key=lambda x: x[1], reverse=True)]
    return " ".join(str(word_sorted.index(word) + 1) for word in word_list)


print(solution('hi hi bye hi cya bye'))
print(solution('hi bye hi cya bye'))
print(solution('aALg aALg aALg aALg aALg oAWleA aALg aALg A aALg'))
