user_input = input('Enter the text to write to a file: ')
file = open('output.txt','r+')
writing_file = file.write(user_input)
print('Data successfully written to output.txt: ', writing_file)
file.close()


#reading the file
file = open('output.txt','r+')
reading_file = file.read()
print(reading_file)
file.close()

#appending the data to the file
user_append_input = input('Enter additional text to append: ')
file = open('output.txt','a')
appending_file = file.write(user_append_input)
print('Data successfully appended:' , appending_file)
file.close()
