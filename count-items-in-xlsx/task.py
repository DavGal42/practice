import xlsxwriter

def get_content(fname):
    with open(fname) as f:
        return f.read()



workbook = xlsxwriter.Workbook('count-items.xlsx')
worksheet = workbook.add_worksheet()

bold = workbook.add_format({'bold': True})

worksheet.write('A1', 'Letters', bold)
worksheet.write('A2', 'Vowels', bold)
worksheet.write('B1', 'Numbers', bold)
worksheet.write('C1', 'Symbols', bold)


def count_items(content):
    vowels = 'aeiou'
    vowel_words = {}
    cons_words = {}
    nums = {}
    symbols = {}
    for item in content.lower():
        if item.isalpha():
            if item in vowels:
                if item in vowel_words:
                    vowel_words[item] += 1
                else:
                    vowel_words[item] = 0
            else:
                if item in cons_words:
                    cons_words[item] += 1
                else:
                    cons_words[item] = 0
        elif item.isdigit():
            if item in nums:
                nums[item] += 1
            else:
                nums[item] = 0
        else:
            if item in symbols:
                symbols[item] += 1
            else:
                symbols[item] = 0
    return vowel_words, cons_words, nums, symbols


def sort_items(vowel_words, cons_words, nums, symbols):
    vowel_words_list = list(vowel_words.items())
    cons_words_list = list(cons_words.items())
    nums_list = list(nums.items())
    symbols_list = list(symbols.items())
    sorted_vowel_words = sorted(vowel_words_list, key= lambda x: x[1], reverse=True)
    sorted_cons_words = sorted(cons_words_list, key= lambda x: x[1], reverse=True)
    sorted_nums = sorted(nums_list, key= lambda x: x[1], reverse=True)
    sorted_symbols = sorted(symbols_list, key= lambda x: x[1], reverse=True)
    return sorted_vowel_words, sorted_cons_words, sorted_nums, sorted_symbols

def get_items(vowel_words, cons_words, nums, symbols):
    vowel_words_list = []
    cons_words_list = []
    nums_list = []
    symbols_list = []
    for item in vowel_words:
        tmp = item[0] + ': ' + str(item[1])
        vowel_words_list.append(tmp)
    for item in cons_words:
        tmp = item[0] + ': ' + str(item[1])
        cons_words_list.append(tmp)
    for item in nums:
        tmp = item[0] + ': ' + str(item[1])
        nums_list.append(tmp)
    for item in symbols:
        tmp = item[0] + ': ' + str(item[1])
        symbols_list.append(tmp)
    return vowel_words_list, cons_words_list, nums_list, symbols_list


def write_words(vowel_words, cons_words):
    row = 2
    for item in vowel_words:
        worksheet.write(row, 0, item)
        row += 1
    worksheet.write(row, 0, 'Consonants', bold)
    for item in cons_words:
        row += 1
        worksheet.write(row, 0, item)

def write_cons_words(cons_words):
    row = 1
    for item in cons_words:
        worksheet.write(row, 0, item)
        row += 1


def write_nums(nums):
    row = 1
    for item in nums:
        worksheet.write(row, 1, item)
        row += 1


def write_symbols(symbols):
    row = 1
    for item in symbols:
        worksheet.write(row, 2, item)
        row += 1


def main():
    cnt = get_content('count-items-in-xlsx/db.txt')
    vowel_words, cons_words, nums, symbols = count_items(cnt)
    vw, cw, n, s = sort_items(vowel_words, cons_words, nums, symbols)
    vwl, cwl, nl, sl = get_items(vw, cw, n, s)
    write_words(vwl, cwl)
    write_nums(nl)
    write_symbols(sl)
    workbook.close()


if __name__ == '__main__':
    main()