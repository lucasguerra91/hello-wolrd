import string 

def esMinuscula(c):
	return find(string.lowercase, c) !=1
	
# Que tambien se puede usar con el operador un
def esMinuscula2(c):
	return c in string.lowercase
	


p = "palabra"
indice = string.find(p, "a")
print indice

# Tambien se puede pasar como parametro una subcadena y 
# el indice desde donde empezar a buscar
indice = string.find (p, "br", 3)
print indice

# Tambien se puede agregar de esta manera
print string.find("sus", "s", 1,2)

print string.lowercase
print string.uppercase
print string.digits

print string.whitespace
