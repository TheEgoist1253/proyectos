full_dot = '●'
empty_dot = '○'




def create_character(name,strength,inte,cha):
    if not isinstance(name,(str)):
        print("The character name should be a string.")
    if name == "":
        print("The character should have a name.")
    if len(name) > 10:
        print("The character name is too long")
    if " " in name:
        print("The character name should not contain spaces")           
    if not isinstance(strength, int) or not isinstance(inte, int) or not isinstance(cha, int):
        print("All stats should be integers")
    if strength < 1 or cha <1 or inte <1:
        print("All stats should be no less than 1")
    if strength > 4 or cha >4 or inte >4:
        print("All stats should be no more than 4")    
    if (strength+inte+cha) != 7:
        print("The character should start with 7 points")
    def bar(value):
        return "●" * value + "○" * (10 - value)
    return (f"{name}\nSTR {bar(strength)}\nINT {bar(inte)}\nCHA {bar(cha)}")    




name = input("Enter name: ")
print("ahora ingrese estadisticas, maximo 7 puntos en total")

try:
    strength = int(input("Strength: "))
    inte = int(input("Intelligence: "))
    cha = int(input("Charisma: "))
except:
    print("All stats should be integers")
else:
    result = create_character(name, strength, inte, cha)
    print(result)
    
         






        
        
            