# The global statement
# modifying global variable from a local function 

def spam():
    global eggs # defining eggs as a global variable
    eggs = 'spam' # modifies the global variable 

eggs = 'global'
spam()
print(eggs)