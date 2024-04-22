def get_content(filename):
    with open(filename) as f:
        return f.read()


stop_words = ['a', 'of', 'on', 'i', 'for', 'with', 'the','at',
              'from','in', 'to', 'is','and','was','as','were']


def count_words(content):
    counter = {}
    items = content.split()

    for el in items:
        if el.isalpha() and el.lower() not in stop_words:
            if el.lower() in counter:
                counter[el.lower()] += 1
            else:
                counter[el.lower()] = 1
    
    return counter


def check_top_num(words):
    while True:
        tops = int(input('Enter a number which should show the top n-th words: '))
        if tops < len(words):
            break
        else:
            print('Wrong number')
    
    return tops


def get_tops(tops, words):
    top_words = []
    for i in range(tops):
        top_words.append(words[i])
    
    return top_words


def main():
    cnt = get_content('five-tasks/word-freq-counter/text.txt')
    counted_words = count_words(cnt)
    sorted_words = sorted(counted_words.items(), key=lambda x: x[1], reverse=True)
    top_num = check_top_num(sorted_words)
    top_words = get_tops(top_num, sorted_words)
    print(top_words)


if __name__ == '__main__':
    main()