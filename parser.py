# [31/Jul/2020 22:30:21] POP3: User rkorolev@jlr-autoplus.ru authenticated  from IP address 192.168.16.15



        

def runner(filename, keyword):
    with open(filename, encoding='utf-8') as file:
        result = list()
        for line in file.readlines():
            line = line.lower().split()
            if searcher(line, keyword):
                str = ' '.join(line)
                str += ' \n'
                result.append(str)
        
        
        return result
            
def searcher(list,kword):
    user = list[4].split('@')[0]
    if user in kword:
        return list
    else:
        return 0

a = runner('text.txt', 'nedopekina@jlr-autoplus.ru')
print(*a)

    