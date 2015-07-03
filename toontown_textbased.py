from random import randint, choice

toon_species = ['dog', 'cat', 'mouse', 'horse', 'bear', 'monkey', 'pig']
species = ''
name = ''
laff = 15
max_laff = 15
tasks = []
task_carry_limit = 1
progress = 0
throw = 1
squirt = 1
throw_inventory = [1, 0, 0, 0, 0, 0, 0]
squirt_inventory = [1, 0, 0, 0, 0, 0, 0]
throwxp = 0
squirtxp = 0
throwxp_gain = 0
squirtxp_gain = 0
task_id = 0

gags = [throw, squirt]
throw_gags = ['cupcake']
squirt_gags = ['squirting flower']

cog_health = 0
cog_level = 1

def showLaff():
    global laff
    print "Laff = %d" % laff


def findHealth(level):
    return (level + 1) * (level + 2)


def clip_on_tie(level):
    global laff
    print "The cog used Clip-On-Tie!"
    phrases = [
        "Better dress for our meeting.",
        "You can't go OUT without your tie.",
        "The best dressed Cogs wear them.",
        "Try this on for size.",
        "You should dress for success.",
        "No tie, no service.",
        "Do you need help putting this on?",
        "Nothing says powerful like a good tie.",
        "Let's see if this fits.",
        "This is going to choke you up.",
        "You'll want to dress up before you go OUT.",
        "I think I'll tie you up."
    ]
    print choice(phrases)
    if level == 1 or level == 2:
        laff -= 1
    elif level == 3:
        laff -= 2
    showLaff()


def pound_key(level):
    global laff
    print "The cog used Pound Key!"
    phrases = [
        "Time to return some calls.",
        "I'd like to make a collect call.",
        "Ring-a-ling - it's for you!",
        "I've been wanting to drop a pound or two.",
        "I have a lot of clout.",
        "This may cause a slight pounding sensation.",
        "I'll just punch in this number.",
        "Let me call up a little surprise.",
        "I'll ring you up.",
        "O.K. Toon, it's the pound for you."
    ]
    print choice(phrases)
    laff = laff - level
    showLaff()


def shred(level):
    global laff
    print "The cog used Shred!"
    phrases = [
        "I need to get rid of some hazardous waste.",
        "I'm increasing my throughput.",
        "I think I'll dispose of you right now.",
        "This will get rid of the evidence.",
        "There's no way to prove it now.",
        "See if you can put this back together.",
        "This should cut you down to size.",
        "I'm going to rip that idea to shreds.",
        "We don't want this to fall into the wrong hands.",
        "Easy come, easy go.",
        "Isn't this your last shred of hope?"
    ]
    print choice(phrases)
    laff -= level * 2
    showLaff()

def cogDie():
    global throwxp
    global throwxp_gain
    global squirtxp
    global squirtxp_gain
    print "You have defeated the cog!"
    if throwxp_gain > 0:
        throwxp += throwxp_gain
        print "You have gained %d throw points! Throw XP = %d" % (throwxp_gain, throwxp)
        throwxp_gain = 0
    if squirtxp_gain > 0:
        squirtxp += squirtxp_gain
        print "You have gained %d squirt points! Squirt XP = %d" % (squirtxp_gain, squirtxp)
        squirtxp_gain = 0
    raw_input("")

def flunky():
    global cog_health
    global cog_level
    if cog_health > 0:
        attack = randint(1, 3)
        if attack == 1:
            clip_on_tie(cog_level)
        elif attack == 2:
            pound_key(cog_level)
        elif attack == 3:
            shred(cog_level)


def pickGag():
    global throw_gags
    global squirt_gags
    global throw_inventory
    global squirt_inventory
    global throwxp
    global squirtxp
    global throwxp_gain
    global squirtxp_gain
    print "Pick a gag:"
    for gag in throw_gags:
        print "Throw: %s - %d" % (gag, throw_inventory[throw_gags.index(gag)])
    for gag in squirt_gags:
        print "Squirt: %s - %d" % (gag, squirt_inventory[squirt_gags.index(gag)])
    loop = 1
    while loop == 1:
        gag = raw_input()
        if gag in throw_gags and throw_inventory[throw_gags.index(gag)] > 0:
            throwxp_gain = throwxp + throw_gags.index(gag) + 1
            throw_inventory[throw_gags.index(gag)] -= 1
            loop = 0
        elif gag in squirt_gags and squirt_inventory[squirt_gags.index(gag)] > 0:
            squirtxp_gain = squirtxp + squirt_gags.index(gag) + 1
            squirt_inventory[squirt_gags.index(gag)] -= 1
            loop = 0
        else:
            print "You need to input a gag that is in your inventory!"
    return gag


def addTask(task):
    global tasks
    tasks.append(task)
    print "Task Added: %s" % task


def toontorial():
    global cog_health
    global species
    global name
    tom = "Tutorial Tom: "
    loop = 0
    while loop == 0:
        name = raw_input(tom + "Hi there! What is your name? ")
        species = raw_input(tom + "What species are you? ")
        if species.lower() not in toon_species:
            species = raw_input(tom + "That's not a species! Please input a species.")
        choice = raw_input(tom + "You are a %s, and your name is %s. Correct? Y/N: " % (species, name))
        if choice.lower() == 'y':
            loop = 1
    raw_input(tom + "Ok %s, as you've probably heard, Toontown has been overrun by cogs!" % name)
    raw_input(tom + "In order to defeat them, you must use your gags to make them happy. They HATE being happy!")
    raw_input(tom + "Gasp! There's a cog outside as we speak! Go defeat that cog!")
    addTask("Defeat a Flunky")
    raw_input("")
    print "You have encountered a Flunky! Pick a gag to damage him!"
    cog_health = 6
    while cog_health > 0:
        gag = pickGag()
        if gag.lower() == 'cupcake':
            print "You threw a cupcake at the Flunky! It did 4 damage!"
            cog_health -= 4
            raw_input("")
            flunky()
        elif gag.lower() == 'squirting flower':
            print "You used a squirting flower on the Flunky! It did 2 damage!"
            cog_health -= 2
            raw_input("")
            flunky()
    cogDie()
    raw_input("Go back to the playground to get more gags!")


def intro():
    print "Welcome to Toontown!"
    print "If you're ready to play, enter '1'."
    print "If you want to quit, enter '2'."
    option = raw_input("")
    if int(option) == 1:
        if progress == 0:
            toontorial()
        else:
            pass
    else:
        print "See you next time!"


intro()
