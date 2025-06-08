try:
    file1 = open ('samples.txt','r')
    reading_file = file1.read()
    print('Reading file content:\n' , reading_file)
    file1.close()

except FileNotFoundError:
    print('The file sample.txt was not found')


