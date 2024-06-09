### 1ml_true

ml_true = [1, 2, 3, 4, 5] 
ml_false = [5, 1, 2, 3, 4] 

def is_sorted(lst):
    if sorted(lst) != lst:
        return False
    return True



### 2

def are_anagrams(str1, str2):
    if len(str1) != len(str2):
        return False
    else:
        mmax = len(str1)

    for i in range(mmax):
        if str1[i] not in str2:
            return False
        else:
            str2 = str2.replace(str1[i], '')
    
    return True




### 3
