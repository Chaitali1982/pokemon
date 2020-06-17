#step 1 ,step 2
class Pokemon:
  def __init__(self, name, level, ptype, is_knocked_out,dead = False,exp = 0):
    self.exp = exp
    self.name = name
    self.level = level
    self.ptype = ptype
    self.is_knocked_out = False
    self.dead = dead
    self.max_health = level*5
    self.health = self.level*5
    #pokemon information
  def __repr__(self):
    return "Pokemon info. {}, current level: {}, type: {}, maximun health: {}, current health: {}.\n".format(self.name, self.level, self.ptype, self.max_health, self.health)  
  #A Pokémon that is knocked out 
  def knock_out(self):
    self.is_knocked_out = True
    if self.health != 0:
      self.health = 0
      print("{name} was knocked out!".format(name = self.name))
  #step 3
  def gain_health(self, heal):
    self.health += heal
    print("{} gained {} health".format(self.name, heal))
    print("{}'s health: {}".format(self.name, self.health))   
  #step 3
  def revive(self):
    if self.is_knocked_out:
      self.is_knocked_out = False
      self.health = 1
      print("{name} has been revived with {health} health!".format(name = self.name, health = self.health))
    else:
      print("{name} is not knocked out.".format(name = self.name)) 
  #step 3
  def lose_health(self, dmg):
    self.health -= dmg
    if self.health <= 0:
      self.health = 0
      self.knock_out() 
#step 4
#A Pokémon that is knocked out should not be able to attack another Pokémon
  def attack(self, other, dmg):
    if self.is_knocked_out == True:
      print("You can not attack. {pokemon} is knocked out!".format(pokemon = self.name))
      return
    if self.ptype == 'Water':
      if other.ptype == 'Fire':
        dmg *= 2
      elif other.ptype == 'Grass':
        dmg /= 2
    elif self.ptype == 'Fire':
      if other.ptype == 'Grass':
        dmg *= 2
      elif other.ptype == 'Water':
        dmg /= 2
    elif self.ptype == 'Grass':
      if other.ptype == 'Water':
        dmg *= 2
      elif other.ptype == 'Fire':
        dmg /= 2
    other.lose_health(dmg)
    print("{} attacked {}".format(self.name, other.name))
    print("{} dealt {} damage to {}. His health is {}.".format(self.name, dmg, other.name, other.health))
#step 9
  def gain_exp(self, exp):
    self.exp += exp
    print("{} gained {} xp.\n".format(self.name, exp))
    if self.exp >= 3:
      self.level_up()
  #step 9
  def level_up(self):
    self.exp = 0
    self.level += 1
    self.max_health += 1
    self.health = self.max_health
    print("{} leveled up to level {}! Max health now is {}. Health fully regenerated.\n".format(self.name, self.level, self.max_health))
    #step 6
class Trainer:
  def __init__(self, name, pokemons, potions, current_pokemon,dead=False):
    self.name = name
    self.pokemons = pokemons
    self.potions = potions
    self.current_pokemon = current_pokemon
    self.dead=dead
    #trainer information
  def __repr__(self):
    return "Trainer info. {name}, has pokemons: {pokemons}, has {potions} potions, current pokemon is {current_pokemon}.".format(name = self.name, pokemons = self.pokemons, potions = self.potions, current_pokemon = self.current_pokemon)
  def use_potion(self):
    if self.potions > 0:
      if self.current_pokemon.health < self.current_pokemon.max_health:
        self.current_pokemon.gain_health(1)
        self.potions -= 1
        print("{} has {} potions left.\n".format(self.name, self.potions))
      else:
        print("{} failed to use a potion on {}. Your pokemon has maximum health.\n".format(self.name, self.current_pokemon.name))
    else:
      print("{}, you have no potions!\n".format(self.name))
  
  def attack(self, other, dmg):
    self.current_pokemon.attack(other.current_pokemon, dmg)
  #A trainer should not be able to switch their active Pokémon to one that is knocked out
  def switch(self, pokemon1):
    self.pokemon1 = pokemon1
    if pokemon1.knock_out is True:
      return print("cannot switch to dead pokemon")
    for i in self.pokemons:
      if self.pokemon1 == i:
        self.current_pokemon = i
        print("{} is now active pokemon".format(self.current_pokemon.name))
       
    
    

class Charmander(Pokemon):
  def __init__(self, name, level, type, is_knocked_out):
    super().__init__(name, level, type, is_knocked_out)
  
 


# The game
pikachu = Charmander("Pikachu", 3, "Fire", False)
bulbasaur = Pokemon("Bulbasaur", 3, "Grass", False)
squirtle = Pokemon("Squirtle", 3, "Water", False)
charmander = Charmander("Charmander", 3, "Fire", False)
vysaur =  Pokemon("vysaur", 3, "Grass", False)
Charizard = Pokemon("Charizard", 3, "Fire", False)
Wartortle = Pokemon("Wartortle", 3, "Water", False)
Blastoise= Pokemon("Blastoise", 3, "Water", False)
Ivysaur =  Pokemon("Ivysaur", 3, "Grass", False)
erika = Trainer('Erika', [pikachu,vysaur,Wartortle], 2, pikachu)
ramos = Trainer('Ramos', [bulbasaur, squirtle,Charmander], 2, bulbasaur)
tina = Trainer('Tina', [Charizard, Blastoise,Ivysaur], 2, bulbasaur)
print("------------------------")
print(erika)
print("------------------------")
print(pikachu)
print("------------------------")
print(bulbasaur)
print("------------------------")
Blastoise.attack(squirtle,12)
print("------------------------")
pikachu.lose_health(1)
print("------------------------")
pikachu.gain_health(1)
print("------------------------")
erika.attack(ramos,2)
print("------------------------")
ramos.attack(erika,2)
print("------------------------")
pikachu.attack(bulbasaur,3)
print("------------------------")
erika.switch(Wartortle) 
print("------------------------")
bulbasaur.gain_exp(3)