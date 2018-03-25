
# coding: utf-8

# In[113]:


import numpy as np
import random


# In[114]:


karten = np.random.randint(1, 5, size=100000)


# In[115]:


class zufall_ohne:
    def __init__(self):
        self.zufall = [1,2,3,4]
    
    def ziehen_ohne(self):
        entfernt = random.choice(self.zufall)
        self.zufall.remove(entfernt)
        return (entfernt)


# In[116]:


einzel = False
statistik = {'erster':0, 'zweiter':0, 'dritter':0 ,'vierter':0}
spielrunden = 0
for i in karten:
    spieler = zufall_ohne()
    if einzel: 
        print("Schwarze Position: " + str(i))
    erster = spieler.ziehen_ohne()
    if einzel: 
        print("   Erster zieht Karte " + str(erster))
    if i == erster:
        statistik['erster'] += 1
        spielrunden += 1
    else:
        zweiter = spieler.ziehen_ohne()
        if einzel: 
            print("   Zweiter zieht Karte " + str(zweiter))
        if i == zweiter:
            statistik['zweiter'] += 1
            spielrunden += 2
        else:
            dritter = spieler.ziehen_ohne()
            if einzel: 
                print("   Dritter zieht Karte " + str(dritter))
            if i == dritter:
                statistik['dritter'] += 1
                spielrunden += 3
            else:
                vierter = spieler.ziehen_ohne()
                if einzel: 
                    print("   Vierter zieht Karte " + str(vierter))
                if i == vierter:
                    statistik['vierter'] += 1
                    spielrunden += 4
    if einzel:
        for (key, value) in statistik.items():
            print(' '*6 + key + ': ' + str(value))

for (key, value) in statistik.items():
    print(key + ': ' + str(round(value/ len(karten),2)* 100) + '%')   
 

