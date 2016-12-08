'''Letters and Numbers
Given an array filled with letters and numbers, find the longest
subarray with an equal number of letters and numbers
'''

def longest_letternumber_array(A):
    longest_sub_array = []
    
    for i in range(len(A)):
        for j in reversed(range(i,len(A))):
            (n_letters,n_numbers) = count_letternum(A[i:j])
            if n_letters == n_numbers:
                break
        if n_letters > len(longest_sub_array)/2:
            longest_sub_array = A[i:j]
    return longest_sub_array

def count_letternum(char_array):
    n_letters = 0
    n_numbers = 0
    for c in char_array:
        if c.isalpha():
            n_letters += 1
        elif c.isdigit():
            n_numbers += 1
    return n_letters, n_numbers

if __name__ == '__main__':
    test_array = list('ks910273ldajp923hwf902398wjf0a9ud20938ufh3901sy9u232790uwahsd98io23jhwkdd')
    print(longest_letternumber_array(test_array))