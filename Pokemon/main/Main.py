from main.Pokemon import Pokemon, Type, Skill

waterType = Type("water", ("electric"), ("fire"))
fireType = Type("fire", ("water"), ("ice"))
airType = Type("air", ("electric"), ("ground"))
dragonType = Type("dragon", ("water"), ("ice"))
physicalType = Type("physical", ("water"), ("ice"))

fireblast = Skill("fireblast", fireType, 15)
skyattack = Skill("skyattack", airType, 10)
dragonbreath = Skill("dragonbreath", airType, 18)
hydrocannon = Skill("hydrocannon", waterType, 20)
skullbash = Skill("skullbash", physicalType, 24)
megapunch = Skill("megapunch", physicalType, 13)

charizard = Pokemon("charizard", fireType, 70, 150, [fireblast, skyattack, dragonbreath])
blastoise = Pokemon("blastoise", waterType, 85, 130, [hydrocannon, skullbash, megapunch])

print charizard
print blastoise

charizard.attack(blastoise, fireblast)
charizard.attack(blastoise, skyattack)

print blastoise
