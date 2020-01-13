# This command opens the content of context.txt and defines it as my_name
with open('name.txt') as f:
    my_name = f.read()

introduction = "Hello, my name is " + my_name

# This command prints the phrase and the variable 

with open('hello.txt', 'w') as f:
    f.write(introduction)
    f.write('\n')

print(introduction)