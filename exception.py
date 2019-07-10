#markdown
#exception handling
try:
    print(100/1)
except FileNoteFoundError:
    print('I am inside exception')
except:
    print('I am Generic Except')
finally:
    print('I am finaly')     
print('I am below division')    