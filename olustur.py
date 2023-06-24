liste = ["Hakan","Emre","Suleyman","Ahmet","OmerFaruk","Levent"]
import os 

for item in liste:
    fPath = fr"Projeler\{item}"
    if not os.path.exists(fPath):
        os.mkdir(fPath)
    
    
