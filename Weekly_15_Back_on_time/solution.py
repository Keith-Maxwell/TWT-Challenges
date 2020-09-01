def solution(dirs):
    if dirs.count('n') == dirs.count('s') and dirs.count('e') == dirs.count('w') and len(dirs) <= 10:
        return True
    return False


print(solution(['n', 'e', 's', 'w']))  # True
print(solution(['e', 'n', 'n', 'w', 's']))  # False
