text = """Imagine if every object we owned retained a physical memory of the moments it witnessed throughout its existence.
The wooden dining table would hold the faint vibrations of decades of family arguments, laughter, and whispered secrets.
Our keys would carry the residual warmth and anxiety of every frantic morning rush out the front door.
A forgotten coffee mug on the shelf would remember the exact depth of sadness during a midnight heartbreak.
Every worn-out sneaker would store the silent rhythm of miles walked in deep, solitary contemplation through city streets.
This unseen emotional telemetry would transform our living spaces into dense, living museums of our own history.
We would walk through our homes surrounded by a quiet, static hum of past versions of ourselves.
Selecting an outfit from the closet would mean choosing which specific day's energy we want to wear again.
An old winter coat might radiate the crisp comfort of a snowy walk taken five years ago today.
Such a reality would make it impossible to truly feel lonely, as every room would echo with presence.
Conversely, minimalism would become a psychological necessity to escape the overwhelming weight of accumulated emotional noise.
People would trade antique furniture not for its aesthetic value, but for the peaceful aura left by strangers.
Thrift stores would become dangerous labyrinths of unpredictable feelings, housing both immense joy and profound, heavy grief.
We might develop a specialized sensory organ or technology just to read and curate these object-bound memories.
Clearing your mind would require clearing your room, wiping the physical slate clean of all past vibrations.
Inherited heirlooms would serve as literal, tangible bridges to ancestors, sharing their exact feelings across generations.
The concept of loss would shift entirely, because a person's essence would remain trapped inside their favorite watch.
Ultimately, we would treat our belongings with far more reverence, knowing they are constantly recording our lives.
Every scratch, stain, and dent would be recognized as a word in a long, silent material biography.
We would finally understand that we do not just use objects; we actively co-author a story with them."""
def s1():
    counter = 0
    for s2 in text:
        if s2.isupper():
            counter+= 1
    return counter
print(s1())
def s3():
    counter2 = 0 
    for s4 in text:
        if s4.islower():
            counter2 += 1
    return counter2
print(s3())    

def w1():
    r1 = text.split()
    counter3 = 0
    user_input = input()
    for w2 in r1:
        if w2 == user_input:
            counter3 += 1
    return counter3
print(w1())

