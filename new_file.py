class PlayerCharacter:
    memb = True
    def __init__(self, name='anonymous', age=0,  health=100, attack_power=1):#, health, attack_power):
        # if self.age > 17:
            self.name = name
            self.age = age
            self.health = health
            self.attack_power = attack_power
    def run(self):
        print(self.name)
        print('run')
        return self.name + str(self.attack_power)
    @classmethod
    def adding_things(cls, num1, num2):
        return num1 + num2
     
# player1 = PlayerCharacter('bob', 20, 100, 10)
# print(player1.adding_things(1, 2))

list1 = [1,2,3]
list1[1] = 5
print(list1)
tuple1 = (1,2,3)
tuple1[1] = 5
print(tuple1)
