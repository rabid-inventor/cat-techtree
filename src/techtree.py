'''
chia cat tech tree demo
an attempt to create comprehensive tech tree using CATs (Chia asset tokens) as 
the prequeisits for each level




ie
sources 

spear blueprint + wood + stone = compeleted spear + spear blue print

here is the questions as there different cats to be created for each type 
so far I think
BLUEP = blueprint cat <- recreated after sucessful spend
COMPNT = component cat  <- destroied on sucessful spend but can only be spent with blueprint type 
COMPITM = completed item cat which can be used elseware like a weapon to arm troops 
            or used to create new items with correct blueprint 
RESOURCE CAT = source for components


BLUEP
Sucessful spend Requires: 
2 or 3 component cats of the correct type
+ 1 completed item cat


Creates:
Recreates itself to show knowledge is leant
Creates Completed item
any remainder components returned to wallet







'''

import config

class coinTypes:
    resourceCoin = 1
    comsumableCoin = 2
    itemCoin = 3
    blueprintCoin = 4
    statCoin = 5
    coinTypeNames = {resourceCoin:"Resource", 
                    comsumableCoin:"Consumable", 
                    itemCoin:"Item", 
                    blueprintCoin:"BluePrint", 
                    statCoin:"Status"}

    def getTypeName(typeId):
        return coinTypes.coinTypeNames[typeId]


#this class wraps the techTreeCoin type to give it dependanties and outputs
#ie a Resource has 0 dependecies but produces Consumables and maybe XP
#modifiers can be added to produce a higher output rate. 

'''
Inputs
techTreeCoin(class) = the coin that needs to be wrapped 
requiredCoins[array] = array of techTreeCoin.treeID's required to make this coin prefixed with the number of coins 
ie. [3, steelConsumableID, LeatherConsumeableID, SmithyItemID]
producedCoins[array] = array of techTreeCoin.treeID's created buy this coin prefixed with the number of coins
ie. [2, SteelSwordID, XPPiontsID, FineWeaponAchievementID]
'''
class techTreeLinks:
    def __init__(self, techTreeCoin, requiredCoins=[0], producedCoins=[0], modifierCoins=[0]):
        self.coin = techTreeCoin
        self.coinName = techTreeCoin.treeName
        self.coinID = techTreeCoin.treeID
        self.requirements = requiredCoins
        self.produce = producedCoins
        self.modifiers = modifierCoins




    


class techTreeCoin:
    def __init__(self, treeID,
                    treeName ="",
                    coinType=None,
                    isCAT=False, 
                    puzzleHash="", 
                    revieledPuzzle="", 
                    puzzleSolution="",
                    modifierHash="",
                    dataHash="", 
                    mojoValue=1):

        self.treeID = treeID
        self.treeName = treeName
        self.coinType = coinType
        self.isCAT = isCAT
        self.puzzleHash = puzzleHash
        self.revieledPuzzle = revieledPuzzle
        self.puzzleSolution = puzzleSolution
        self.mojoValue = mojoValue 
        self.readyToDeploy = False

#returns a human readable name for the coin
    def getTreeName(self):
        return self.treeName

    def setPuzzleHash(self, puzzleHash=""):
        self.puzzleHash = puzzleHash
    
    

    

    


class techTree:
    def __init__(slef):
        self.maxID=0
        self.coins = []
        self.linkedCoins = [] 
        pass
    
    def addCoin(self, coin):
        self.coins.append(coin)

    def addLinkedCoin(self, coin):
        self.linkedCoins.append(coin)
    

    def getCoinById(self, coinID):
        for coin in coins:
            if (coin.coinID == coinID):
                return coinID
        
        return -1
    
    