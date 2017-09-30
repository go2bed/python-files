f = open('test.txt')
s = f.read()
print(s)
s = f.read()  # The python will read the file only one time and then we need to reset a cursor
print(s)

f.seek(0)  # Reset to begin of the file
s = f.read()
print(s)  # And then t is read again

f.seek(0)
v = f.readlines()
print(v)  # It is a list of lines

new_file = open('new_file.txt', 'w')  # write to the new_file
new_file.write('1 line')
new_file.write('\n')
new_file.write('2 line')
new_file.close()

for line in open('new_file.txt'):
    print(line)

