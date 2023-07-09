
dwarfs=["Doc", "Dopey", "Bashful", "Grumpy"]

def roll_call_dwarves(dwarfs):
    index=1
    for dwarf in dwarfs:
        print(f"{index}. {dwarf}")
        index+=1

def summon_captain_planet(planeteers):
    newlist=[]
    for planeteer in planeteers:
        newlist.append(planeteer.capitalize() + "!")
    return newlist
    

def long_planeteer_calls(calls):
    found="no"
    for call in calls:
        if len(call) > 4:
            found="yes"
    longer_than_four=True if found == "yes" else False   
    return longer_than_four 

 
def find_the_cheese(food):
    cheese=["cheddar","gouda","camembert"]
    item_found="no"
    for item in food:
       if item in cheese:
          item_found="yes"
          return item
    if item_found == "no": return None
print(find_the_cheese(["ham", "cellphone", "computer"]))