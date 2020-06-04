# Cette fonction ne sert pas vraiment, on la considère void, elle ne renvoit rien
def modify_string(string):
    string += " La fonction modify string a été appelée"


def modify_string_return(string):
    return string + " La fonction modify string a été appelée et retournée"


test = "This is a test"
print(test)
modify_string(test)
print(test)
test = modify_string_return(test)
print(test)

# Attention à la portée :
var = 0
exist = False
if exist:
    var = 1234
print(var)
