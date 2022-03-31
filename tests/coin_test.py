from test import *
# importing the sys module
import sys        
 
# appending the directory of mod.py
# in the sys.path list
sys.path.append('/home/geeus81/chiadev/git/cat-techtree/src/') 

from techtree import *

evo = techTree(techTreeName="BasicEvo")


#testcoin set 
resForest = techTreeCoin(1, treeName="Forest",coinType=coinTypes.resourceCoin)
resQuary = techTreeCoin(2, treeName="Quarry",coinType=coinTypes.resourceCoin)
resPond = techTreeCoin(3, treeName="Pond",coinType=coinTypes.resourceCoin)

comsLumber = techTreeCoin(4, treeName="Lumber", coinType=coinTypes.comsumableCoin)
comsFlint = techTreeCoin(5, treeName="Flint", coinType=coinTypes.comsumableCoin)
comsNappedFlint = techTreeCoin(6, treeName="Flint", coinType=coinTypes.comsumableCoin)


bluePointyStick = techTreeCoin(10, treeName="Sharp pointy stick", coinType=coinTypes.blueprintCoin)
blueFlintnapping = techTreeCoin(7, treeName="flint napping", coinType=coinTypes.blueprintCoin)
blueFlintAxe = techTreeCoin(8, treeName="Flint sharpened Axe Blueprint", coinType=coinTypes.blueprintCoin)


itemSFAxe = techTreeCoin(9, treeName="Sharped Flint Axe", coinType=coinTypes.itemCoin)


#create some links 


linkresForest = techTreeLinks(resForest, requiredCoins=[0], producedCoins=[4], modifierCoins=[10])


def test_resouce_coin():
    resForest = techTreeCoin(1, treeName="Forest",coinType=coinTypes.resourceCoin)
    assert resForest.coinType == 1
    assert coinTypes.getTypeName(resForest.coinType) == "Resource"


def test_coin_deps():
    evo.addLinkedCoin(linkresForest)
    grabbedCoin = evo.getCoinById(linkresForest.coinID)
    assert grabbedCoin.coinName == "Forest"
    



#run tests 
test_resouce_coin()
test_coin_deps()