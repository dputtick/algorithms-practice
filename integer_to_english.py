import itertools


def int_to_english(n):
    ones = {'1': 'one',
            '2': 'two',
            '3': 'three',
            '4': 'four',
            '5': 'five',
            '6': 'six',
            '7': 'seven',
            '8': 'eight',
            '9': 'nine'}
    teens = {'0': 'ten',
            '1': 'eleven',
            '2': 'twelve',
            '3': 'thirteen',
            '4': 'fourteen',
            '5': 'fifteen',
            '6': 'sixteen',
            '7': 'seventeen',
            '8': 'eighteen',
            '9': 'nineteen'}
    tens = {'2': 'twenty',
            '3': 'thirty',
            '4': 'forty',
            '5': 'fifty',
            '6': 'sixty',
            '7': 'seventy',
            '8': 'eighty',
            '9': 'ninety'}
    bigs = {1: 'thousand',
            2: 'million',
            3: 'billion',
            4: 'trillion',
            5: 'quadrillion',
            6: 'quintillion',
            7: 'sextillion',
            8: 'septillion',
            9: 'octillion'}
    def check_triplet(index, triplet):
        acc = []
        if all(num == 0 for num in triplet):
            return None
        if len(triplet) < 3:
            triplet = [0] * (3-len(triplet)) + triplet
        for j, digit in enumerate(triplet):
            if digit == '0':
                continue
            if j == 0:
                acc.append(ones[digit])
                acc.append('hundred')
                continue
            if j == 1:
                if digit == '1':
                    acc.append(teens[triplet[2]])
                    continue
                acc.append(tens[digit])
                continue
            if j == 2:
                if triplet[1] == '1':
                    continue
                acc.append(ones[digit])
        if index in bigs:
            acc.append(bigs[index])
        return acc
    reversed_str_list = list(reversed(str(n)))
    split_up = [reversed_str_list[i:i+3][::-1] for i in range(0, len(reversed_str_list), 3)]
    result_list = []
    for index, triplet in enumerate(split_up):
        if check_triplet(index, triplet):
            result_list.insert(0, check_triplet(index, triplet))
    flattened_list = list(itertools.chain(*result_list))
    return ' '.join(flattened_list)


if __name__ == '__main__':
    print(int_to_english(103))