def summon_captain_planet(planeteers):
    newlist=[]
    for planeteer in planeteers:
         newlist.append(planeteer.capitalize() + "!")
    return newlist

print(summon_captain_planet(["carrot", "cucumber", "pepper"]))    