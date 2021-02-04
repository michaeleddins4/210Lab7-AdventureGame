from flask import Flask, render_template, url_for, redirect, request, flash
import random
app = Flask(__name__)
app.secret_key = "student3"

boss_hp = 125
boss_strength = 20
boss_status = 0

startroomstatus = 0
room4status = 0
room6status = 0
room8status = 0

points = 0
health = 100
strength = 20

monster_1_hp = 40
monster_2_hp = 45
monster_3_hp = 50

monster_1_strength = 9
monster_2_strength = 10
monster_3_strength = 12

items = {"Basic sword"}

monster1status = 1
monster2status = 1
monster3status = 1

@app.route("/fight1")
def fight1():
    global monster_1_hp
    global monster_1_strength
    global items
    global points
    global health
    global strength
    global monster1status
    if (monster_1_hp > 0 and health > 0):
        room = "Time to fight!"
        desc = """This Naga is going down.. Hit the 'fight' button to trade blows with the monster!"""
        monster_1_hp = (monster_1_hp - random.randint(0, strength))
        health = (health - random.randint(0, monster_1_strength))        
        exits = { "fight" : "/fight1" }
        return render_template("room.html", name=room, description=desc, rooms=exits, hp=health, st=strength, inv=items, score=points, monhp=monster_1_hp, monst=monster_1_strength)
    
    elif (monster_1_hp <= 0):
        room = "You got him!"
        desc = """The Naga falls to the ground, beaten and bloodied. You have some pretty bad wounds yourself.. Hopefully you can find something to patch yourself up.. You can either go:"""
        exits = { "west" : "/room4", "north" : "/room3", "east" : "/" } 
        monster1status = 0
        points = (points + 100 + 40 + health)
        strength = strength + 5
        return render_template('room.html', name=room, description=desc, rooms=exits, hp=health, st=strength, inv=items, score=points)

    elif (health <= 0):
        room = "You died"
        desc = """Unfortunate.. You failed to escape. Would you like to try again?"""
        exits = { "restart" : "/" }
        points = 0
        health = 100
        strength = 20
        monster_1_hp = 40
        monster_2_hp = 45
        monster_3_hp = 50
        boss_hp = 125
        items = {"Basic sword"}
        monster1status = 1
        monster2status = 1
        monster3status = 1 
        room4status = 0
        room6status = 0
        room8status = 0
        startroomstatus = 0
        return render_template('room.html', name=room, description=desc, rooms=exits, hp=health, st=strength, inv=items, score=points)

@app.route("/fight2")
def fight2():
    global monster_2_hp
    global monster_2_strength
    global items
    global points
    global health
    global strength
    global monster2status
    global room6status
    if (monster_2_hp > 0 and health > 0):
        room = "Here he comes!"
        desc = """This guy doesn't know what's in store for him. Hit the 'fight' button to trade blows with him!"""
        monster_2_hp = (monster_2_hp - random.randint(0, strength))
        health = (health - random.randint(0, monster_2_strength))
        exits = { "fight" : "/fight2" }
        return render_template("room.html", name=room, description=desc, rooms=exits, hp=health, st=strength, inv=items, score=points, monhp=monster_2_hp, monst=monster_2_strength)

    elif (monster_2_hp <= 0 and room6status == 1):
        room = "You took him down!"
        desc = """The lizardman falls to the ground.. You took a beating as well, but at least you aren't him.. You've gotta get out of here, fast.. You can go:"""
        exits = { "north" : "/room9", "west" : "/room8", "south" : "/room1" }
        monster2status = 0
        points = (points + 120 + 45 + health)
        strength = strength + 5
        return render_template('room.html', name=room, description=desc, rooms=exits, hp=health, st=strength, inv=items, score=points)

    elif (monster_2_hp <= 0):
        room = "You took him down!"
        desc = """The lizardman falls to the ground.. You took a beating as well, but at least you aren't him.. You've gotta get out of here, fast.. You can go:"""
        exits = { "west" : "/room8", "south" : "/room1" }
        monster2status = 0
        points = (points + 120 + 45 + health)
        strength = strength + 5
        return render_template('room.html', name=room, description=desc, rooms=exits, hp=health, st=strength, inv=items, score=points)

    elif (health <= 0):
        room = "You died"
        desc = """Unfortunate... Would you like to try again?"""
        exits = { "restart" : "/" }
        points = 0
        health = 100
        strength = 20 
        monster_1_hp = 40
        monster_2_hp = 45
        monster_3_hp = 50
        boss_hp = 125
        items = {"Basic sword"}
        room4status = 0
        room6status = 0
        room8status = 0
        startroomstatus = 0
        monster1status = 1
        monster2status = 1
        monster3status = 1 
        return render_template('room.html', name=room, description=desc, rooms=exits, hp=health, st=strength, inv=items, score=points)

@app.route("/fight3")
def fight3():
    global monster_3_hp
    global monster_3_strength
    global items
    global points
    global health
    global strength
    global monster3status
    if (monster_3_hp > 0 and health > 0):
        room = "Get ready!"
        desc = """He might be intimidating, but you're stronger. Take him down! Hit the 'fight' button to trade blows with him!"""
        monster_3_hp = (monster_3_hp - random.randint(0,strength))
        health = (health - random.randint(0, monster_2_strength))
        exits = { "fight" : "/fight3" }
        return render_template("room.html", name=room, description=desc, rooms=exits, hp=health, st=strength, inv=items, score=points, monhp=monster_3_hp, monst=monster_3_strength)
        
    elif (monster_3_hp <= 0):
        room = "Demon down!"
        desc = """Hell yeah! (pun intended) You got him! You took some damage, but it's shallow enough to where you can walk it off. Get going! Take a look around the room.. Looks like there's just the door you came in from and a very cracked wall.. You approach the wall, it seems to be pretty drafty. What will you do?"""
        if (strength >=30):
            desc = desc + " You feel strong enough to break it!"
            exits = { "west" : "/room2", "south" : "/room6" }
        else:
            desc = desc + " You don't feel strong enough to break the wall.."
            exits = { "west" : "/room2" }
        monster3status = 0
        points = (points + 150 + 50 + health)
        strength = strength + 5
        return render_template('room.html', name=room, description=desc, rooms=exits, hp=health, st=strength, inv=items, score=points)

    elif (health <= 0):
        room = "You died"
        desc = """Unfortunate.. Would you like to try again?"""
        exits = { "restart" : "/" }
        points = 0
        health = 100
        strength = 20
        monster_1_hp = 40
        monster_2_hp = 45
        monster_3_hp = 50
        boss_hp = 125
        items = {"Basic sword"}
        monster1status = 1
        monster2status = 1
        monster2status = 1
        room4status = 0
        startroomstatus = 0
        room6status = 0
        room8status = 0
        return render_template('room.html', name=room, description=desc, rooms=exits, hp=health, st=strength, inv=items, score=points)

@app.route("/fight4")
def fight4():
    global boss_hp
    global boss_strength
    global items
    global points
    global health
    global strength
    global bossstatus
    if (boss_hp > 0 and health > 0):
        room = "It all comes down to this.."
        desc = """Get this sucker and get out of here! Hit the 'fight' button to trade blows with the monster!"""
        boss_hp = (boss_hp - random.randint(0,strength))
        health = (health - random.randint(0, boss_strength))
        exits = { "fight" : "/fight4" }
        return render_template("room.html", name=room, description=desc, rooms=exits, hp=health, st=strength, inv=items, score=points, monhp=boss_hp, monst=boss_strength)

    elif (boss_hp <= 0):
        room = "You're free! You also destroyed an ancient evil along the way.."
        desc = """You step over the corpse of the fallen demon, badly wounded.. You stumble as you reach for the key around his neck, putting it into the controls and unlocking the door mechanism. You walk up an enormous series of stone stairs, emerging on the surface. YOU ESCAPED!"""
        points = (points + 1000 + 100 + health)
        strength = strength + 5
        exits = { }
        return render_template('room.html', name=room, description=desc, hp=health, rooms = exits, st=strength, inv=items, score=points)
 
    elif (health <= 0):
        room = "You died"
        desc = """Unfortunate.. You were so close. Would you like to try again?"""
        exits = { "restart" : "/" }
        points = 0
        health = 100
        strength = 20
        monster_1_hp = 40
        monster_2_hp = 45
        monster_3_hp = 50
        boss_hp = 125
        room4status = 0
        room6status = 0
        room8status = 0
        items = {"Basic sword"}
        monster1status = 1
        monster2status = 1
        monster2status = 1
        startroomstatus = 0
        return render_template('room.html', name=room, description=desc, rooms=exits, hp=health, st=strength, inv=items, score=points)

@app.route("/")
def start():
    global startroomstatus
    if (startroomstatus == 0): 
        room = "'Wait, where am I?'"
        desc = """You wake up in a cold, dark room with stone walls and a wooden floor, lit by a single candle in the middle of the room. You feel around your surroundings and find a set of basic adventuring gear, some armor and a small iron sword. You take a few practice swings in the dark before preparing to make the adventure in escaping this place. You have a few options of where to go: Each door looks alike in the dark, so you squint to make them out. You see before you a room toward the West, East, and South of you. Which do you choose?"""
        startroomstatus = 1
    else:
        room = "Back here?"
        desc = """This room is just as boring as you remember.. Move on and escape! You can go:"""
    exits = { "west" : "/room1", "east" : "/room2", "south" : "/room7" }
    return render_template('room.html', name=room, description=desc, rooms=exits, hp=health, st=strength, inv=items, score=points)

@app.route("/room1")
def room1():
    if (monster1status == 1):
        room = "Something in the dark.."
        desc = """You step through the door you've chosen, squinting to be able to see through the darkness. You enter the room and hear some shuffling in the opposite corner. Is it someone else that has been trapped down here? You call out but hear no answer outside of a loud hissing noise. Ahead of you is a large Naga shaman, a large creature with a humanoid torso and a snake body, threatening you with a hooked sword. It looks like your only choice is to fight, so get ready!"""
        exits = { "fight" : "/fight1" }   
        return render_template("room.html", name=room, description=desc, rooms=exits, hp=health, st=strength, inv=items, score=points, monhp=monster_1_hp, monst=monster_1_strength)
    
    else:
        room = "Is he still alive?"
        desc = """You come back through the door, stepping over the corpse of the creature that you have bested in battle. There isn't really anything interesting left in this room, so where will you go next?"""   
        exits = { "north" : "/room3", "west" : "/room4", "east" : "/" }
        return render_template("room.html", name=room, description=desc, rooms=exits, hp=health, st=strength, inv=items, score=points)

@app.route("/room2")
def room2():
    desc = """You step through the door, being careful of any traps or creatures that might be lurking around. The room you've just entered has a few torches on the wall, making it easy to see that there is nothing of note in this room, just a few barrels and chairs with a small table, containing another candle in the center. You ponder on the whereabouts of this place and how you ended up here as you look to the path before you. You can either head:"""
    room = "An empty room?"
    exits = { "west" : "/", "east" : "/room5" }
    return render_template("room.html", name=room, description=desc, rooms=exits, hp=health, st=strength, inv=items, score=points)

@app.route("/room3")
def room3():
    global monster_2_strength
    global monster_2_hp
    if (monster2status == 1):
        room = "Wait, what is that?"
        desc = """You step into the room, seeing that this one is much more heavily lit. Upon further inspection, you see a large lizardman sitting at one of those tables having a drink. The second you open your mouth to make peace with the creature, he hisses and lunges toward you with a dagger. Quick, retaliate!"""
        exits = { "fight" : "/fight2" } 
        return render_template("room.html", name=room, description=desc, rooms=exits, hp=health, st=strength, inv=items, score=points, monhp=monster_2_hp, monst=monster_2_strength)

    else:
        room = "'So I'm back here?'"
        desc = """You take another look around the room after you step in, noting nothing interesting but the corpse of the lizardman that you were forced to kill. Whatever he was drinking smells pretty sweet, but you remember you have better things to do. Like... Escape. There's a suspiciously large door with a huge lock in the middle.. Maybe you need a key to pass?"""
        if (room6status == 1):
            exits = { "north" : "/room9", "west" : "/room8", "south" : "/room1" }
        else:
            exits = { "west" : "/room8", "south" : "/room1" }
        return render_template("room.html", name=room, description=desc, rooms=exits, hp=health, st=strength, inv=items, score=points)

@app.route("/room4")
def room4():
    global room4status
    global health
    if (room4status == 0):
        room = "A potion?"
        desc = """As you walk in the room, which is much smaller than the others, you see that it is very well lit. 'Maybe that Naga was guarding something important,' you think before approaching the small pedestal at the end of a large, deep red carpet. It's a bright red liquid in a bottle. You make sure it isn't booby trapped before picking it up and inspecting it, swirling it around the bottle. You take a whiff of it and decide that it's safe, downing the entire thing in a few chugs. Suddenly you feel like your wounds from the previous bout(s) are healing!"""
        exits = { "east" : "/room1" }
        room4status = 1
        health = health + 100
        return render_template("room.html", name=room, description=desc, rooms=exits, hp=health, st=strength, inv=items, score=points)
    
    else:
        room = "Just checking"
        desc = """You take another look around the room to see if anything else of note is to be found, but unfortunately the potion was the only thing here that can help you on your adventure."""
        exits = { "east" : "/room1" }
        return render_template("room.html", name=room, description=desc, rooms=exits, hp=health, st=strength, inv=items, score=points)

@app.route("/room5")
def room5():
    global strength
    global monster_3_hp
    global monster_3_strength
    global room6status
    if (monster3status == 1):
        desc = """You peek into the room before hearing a loud growling noise.. You shut the door quickly before realizing that you probably have to go this way to get free, so you face the large demon that's halting your progress. The room is basked in a red glow as the large, yet spindly demon with a small head and large claws that are able to inflict massive damage are bared. You ready your sword and get ready for an intense battle to the death."""
        room = "Here we go again.."
        exits = { "fight" : "/fight3" }
        return render_template("room.html", name=room, description=desc, rooms=exits, hp=health, st=strength, inv=items, score=points, monhp=monster_3_hp, monst=monster_3_strength)
    
    else:
        room = "This place again.."
        if(strength >= 30):
            desc = """You look around the red-lit room, there is only the one door.. Could there be some other way to progress? You look closer at one of the walls seeing that it has many deep cracks running through it. You feel a draft through the cracks.. Can you break through?"""
            exits = { "west" : "/room2", "south" : "/room6" }
        
        elif(room6status == 1):
            desc = """You've gotten the key from the wall.. Now where should you go? Surely there's somewhere that this key must fit.."""
            exits = { "west" : "/room2", "south" : "/room6" }

        else:
            desc = """You look around the red-lit room, there is only one door.. Could there be some other way to progress? You look closer at one of the walls seeing that it has many deep cracks running through it. You feel a draft through the cracks.. You don't feel strong enough to break through the wall.."""
            exits = { "west" : "/room2" }
        return render_template("room.html", name=room, description=desc, rooms=exits, hp=health, st=strength, inv=items, score=points)

@app.route("/room6")
def room6():
    global room6status
    global items
    if (room6status == 0):
        items.add("Key")
        room6status = 1
        room = "A key?"
        desc = """BANG! You take the wall down! You take a step in, it looks safe.. You walk further into the large hole that you've made in the wall. A corridor lies behind it, in which you traverse down. You find a large, golden key on a pedestal. You make sure it isn't trapped and pick it up, placing it in your bag. Lucky find!"""
        exits = { "north" : "/room5" }
    else:
        room = "Nothing here.."
        desc = """You walk down the corridor once again, not finding anything new.. There must be another way."""
        exits = { "north" : "/room5" }
    return render_template("room.html", name=room, description=desc, rooms=exits, hp=health, st=strength, inv=items, score=points)

@app.route("/room7")
def room7():
    global points
    room = "A.. Cat?"
    desc = """You have a good feeling about this one... You open the door slowly and see a homey, well lit room. Like the room you woke up in, there's a lone table in the middle of the room, in which.. A cat bed is laying? You walk over to the cat, it purrs as it sees you. You reach out and pet the cat on the head. The cat gives you points. Wait, points? What do you need those for, you need to escape this place!"""
    points = points + 220
    exits = { "north" : "/" }
    return render_template("room.html", name=room, description=desc, rooms=exits, hp=health, st=strength, inv=items, score=points)

@app.route("/room8")
def room8():
    global room8
    global strength
    global items
    if (room8status == 0):
        room = "A new weapon!"
        desc = """You step into the room.. This one looks way different, marble floors, large columns, pews lined up in rows leading to a large pedestal. Is this a chapel? You walk over to the pedestal and see the most beautiful sword you've ever laid eyes on. You pick it up and raise it above your head He-Man style. You feel much more powerful already."""
        room8 = 1
        strength = strength + 12
        items.add("Holy Sword")
        exits = { "east" : "/room3" }
        return render_template("room.html", name=room, description=desc, rooms=exits, hp=health, st=strength, inv=items, score=points)

    else:
        room = "The chapel again?"
        desc = """Have you come to pray? You need to escape, remember?!"""
        exits = { "east" : "/room3" }
        return render_template("room.html", name=room, description=desc, rooms=exits, hp=health, st=strength, inv=items, score=points)

@app.route("/room9")
def room9():
    room = "Why do I hear boss music?"
    desc = """You use the key that you got a bit ago and slide it in the giant lock in the middle of the large door.. You creak it open and see a hooded figure.. The powerful demon throws the hood off his head and turns to face you with a large toothy grin on his face. He knew it would come down to this, and he's been looking forward to it. You see the way out right behind him.. But it's locked with bars, and it looks like he's got the key to the mechanism.. Time to end this."""
    exits = { "fight" : "/fight4" }
    return render_template("room.html", name=room, description=desc, rooms=exits, hp=health, st=strength, inv=items, score=points)


app.run(host='0.0.0.0', port=6003, debug=True)
