import random
import fastapi from FastAPI
from pydantic import BaseModel

api = FastAPI() # get api running

# basic fact class
class Fact(BaseModel):
    id: int # numerical id
    fact: str # the fact

# Dreamcast facts cuz why not
facts = [
    Fact(id=0, fact="The dreamcast was almost named 'katana'."),
    Fact(id=1, fact="Despite failing in the US market 18 months after launch, it sold more than the Wii U."),
    Fact(id=2, fact="After making proprietary GD-ROM disk format, the console still played CDs, allowing easy piracy with burned disks."),
    Fact(id=3, fact="With previous SEGA consoles, they gave lopsided deals to EA. With the dreamcast, they switched to 2k sports"),
    Fact(id=4, fact="Considering the dreamcast released in 1998, it's impressive to consider it had online gaming and services out the box."),
    Fact(id=5, fact="SEGA helped Microsoft design XBox prototypes, which almost brought backwards compatibility between the systems"),
    Fact(id=6, fact="There is a version of windows made for the dreamcast."),
    Fact(id=7, fact="The dreamcast memory units could be taken out and used as little handheld consoles."),
    Fact(id=8, fact="There is a dreamcast mouse and keyboard periphial."),
    Fact(id=9, fact="In an era before HDTVs, a VGA/Composite adaptor was made that allowed it to display in a blinding 480p, and link to PC monitors."),
    Fact(id=10, fact="The last offical game released for dreamcast was in 2007."),
    Fact(id=11, fact="Since the dreamcast can run burned disks, lots of people are making homebrew games for the console still."),

# basic get, random or id
@api.get("/fact")
async def get_fact(i):
    if i == None: #if base, give the random
        i = random.randint(0, len(facts) - 1)
    else: # just in case strings
        i = int(i)
    return facts[i]

# only ID endpoint
@api.get("/fact/{id}")
async def get_id(i): # take id
    return facts[int(i)] # return fact of id, wwithout letting strings mess it up

# new fact add
@api.post("/add/")
async def add_fact(fact): # take the new fact
    new_fact = Fact(id=len(facts), fact=fact) # make the fact object
    facts.append(new_fact) # append