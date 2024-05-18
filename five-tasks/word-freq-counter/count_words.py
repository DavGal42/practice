'''

Author: David Galstyan
Date: 28.04.2024
Description: This code count words except stop words and returns top n words

'''


def get_content(filename):
    '''
    
        Description: reads the information of the file
        Parameters: Name of the file
        Returns: information of the file
    
    '''

    with open(filename) as f:
        return f.read()
    

stop_words = ['a', 'of', 'on', 'i', 'for', 'with', 'the','at',
              'from','in', 'to', 'is','and','was','as','were']


def count_words(content):
    '''
    
        Description: counts each word which is not stop word
        Parameters: information of the file
        Returns: each counted word in dict
    
    '''

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
    '''
    
        Description: gives a number of top and checks if it is valid number or not
        Parameters: counted words
        Returns: a given number
    
    '''

    while True:
        tops = int(input('Enter a number which should show the top n-th words: '))
        if tops < len(words):
            break
        else:
            print('Wrong number')
    
    return tops


def get_tops(tops, words):
    '''
    
        Description: gives top n words
        Parameters: number of top; counted words
        Returns: top n words
    
    '''
        
    top_words = []
    for i in range(tops):
        top_words.append(words[i])
    
    return top_words


def main():
    '''
    
        Description: The main function
        Parameters: None
        Returns: top n words
    
    '''
        
    cnt = get_content('five-tasks/word-freq-counter/text.txt')
    counted_words = count_words(cnt)
    sorted_words = sorted(counted_words.items(), key=lambda x: x[1], reverse=True)
    top_num = check_top_num(sorted_words)
    top_words = get_tops(top_num, sorted_words)
    print(top_words)


if __name__ == '__main__':
    main()