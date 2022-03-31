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
                    treeName ="",#Human Readable name for the coin 
                    coinType=None,#Coin Type ie Resource
                    isCAT=False, #Conforms to a TAIL of the CAT1 Standard
                    puzzleHash="", #The coins puzzleHash 
                    revieledPuzzle="", #Serialized version of the full puzzle of the coin
                    puzzleSolution="", #Serialized Version of the soltuion to spend this coin 
                    canModify=False, #Set if coin and be used as a modifier for another coin IE. Axe increase forest lumber production rate
                    canBeModified=False, #Set if coin can recieve a modifier to increase output value or speed
                    modifierHash="", #Hash of the unlock value 
                    modifierFactor=1, #What factor does this coin modify another production by  
                    dataHash="", # Hash of aributes associated with this coin. 
                    mojoValue=1): #Coins mojo value 

        self.treeID = treeID
        self.treeName = treeName
        self.coinType = coinType
        self.isCAT = isCAT
        self.puzzleHash = puzzleHash
        self.revieledPuzzle = revieledPuzzle
        self.puzzleSolution = puzzleSolution
        self.canModify = canModify
        self.canBeModified = canBeModified
        self.modifierHash = modifierHash
        self.modifierFactor = modifierFactor
        self.dataHash = dataHash
        self.mojoValue = mojoValue 
        self.readyToDeploy = False


#returns a human readable name for the coin
    def getTreeName(self):
        return self.treeName

    def setPuzzleHash(self, puzzleHash=""):
        self.puzzleHash = puzzleHash
    
class techTree:
    def __init__(self, techTreeName="Default"):
        self.techTreeName = techTreeName
        self.maxID=0
        self.coins = []
        self.linkedCoins = [] 
        pass
    
    def addCoin(self, coin):
        self.coins.append(coin)

    def addLinkedCoin(self, coin):
        self.linkedCoins.append(coin)
        self.maxID += 1
    

    def getCoinById(self, coinID):
        for coin in self.linkedCoins:
            if (coin.coinID == coinID):
                return coin
        
        return -1
    
    
    class coinUtils:

        def displayCoinInfo(coin):
            print("""
            Coin Info
            CoinType: {0}
            CoinID: {1}
            CoinName: {2}
            Is Coin CAT: {3}
            Coin Puzzle Hash: {4}
            Coin Serialized Puzzle {5}
            Coin Serialized Solution {6}
            """.format(coin.coinType, coin.treeID, coin.treeName, coin., coin., coin.))