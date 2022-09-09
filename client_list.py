
def main():
    infile = open('clients.txt', 'r')

    number = 1
    for line in infile:
        print(number, '. ', line.rstrip('\n\)'), sep='')
        number+=1

main()

