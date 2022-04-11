
# [31/Jul/2020 22:30:21] POP3: User rkorolev@jlr-autoplus.ru authenticated  from IP address 192.168.16.15


def searcher(list,kword):
    if kword in list:
        return list
    else:
        return 0

        


with open('text.txt', encoding='utf-8') as file:
    result = list()
    for line in file.readlines():
        line = line.split()
        if searcher(line, 'nedopekina@jlr-autoplus.ru'):
            str = ' '.join(line)
            str += ' \n'
            result.append(str)
    
    
    print(*result)
        



    