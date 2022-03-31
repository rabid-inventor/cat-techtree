# cat-techtree
A toolset for writing a technology tree in CATs for the Chia blockchain

-CAT types
Resource <- A finite quantity which creates Consumables 
Consumable <- Used to create Items or other Consumables with correct blueprint consumed when used 
Item <- Can be used to modify Resourses or other items created by blueprints 
BluePrint <- used with Items and consumables to create new items
Status <- Used to log points Experinace or rewards could also be used to trade for blueprints


As an example:

#Gaining Consumables
Resource(Forest)1000 -> spend -> Consumable(Lumber)1 + Resource(Forest)999
Resource(Quarry)1000 -> spend -> Comsumable(Stone)1  + Resource(Quarry)999

#Processing Consumables
Blueprint(Flint Napping)1 + Comsumable(Stone)1 -> spend -> Blueprint(Flint Napping)1 + Comsumable(Sharpened Flint)1

#Creating Items
Blueprint(Flint Axe)1 + Comsumable(Sharpened Flint)1 + Comsumable(Lumber)1 -> spend -> Blueprint(Flint Axe)1 + Item(Flint Axe)1 + Status(XP)1

#Increase Consumable Production
Resource(Forest)1000 + Item(Flint Axe)1 -> spend -> Consumable(Lumber)2 + Resource(Forest)998 + Item(Flint Axe)1


Trading:
Accumulated XP could be trading via offer files for more resources or even special items. Status could be used in such a way.

official
Item(dwelling)5 + Item(Tavern)1 + Status(XP)100 -> offered -> Item(Hamlet)1 + Status(SettlerToken)1 


Items Have attributes
ATTACK  
DEFENCE
WEALTH
VALUE
more to be added

Which could allow for a later combat system (not entirely figured out yet)
Item(Soldier) ATK 1 DEF 1 + Item(Broze Sword) ATK 2 DEF 1 + Blueprint(Battle Ogre) ATK 2 DEF 2 -> spend ->  Item(Soldier) ATK 1 DEF 1 + Item(Broze Sword) ATK 2 DEF 1 + Blueprint(Battle Ogre) + Status(XP) + Consumable(Ogre Teeth) 


 