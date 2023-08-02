# Music Tracker Class Design recipe:
## 1. Describe the Problem

_put or write the user story here. Add any clarification notes you might have.
> As a user
> So that I can keep track of my music listening
> I want to add tracks I've listened to and see a list of them.

## 2. Design the class interface 
_Include the initializer, public properties, and public methods with all 
parameters, return values and side-effects
'''
Python
class MusicTracker():
    def __init__(self):
        pass

    def add_music(self, track):
        # Parameters:
        # add: (str) human readable string, representing a music
        pass

    def get_listened_music(self):
        # Returns:
        # A list of incomplete tracks 
        pass
    
    

'''
## Create Examples as Tests
_May be a list of examples of how the class will behave different situations
'''
python
Initially, there are no music added
'''
music_tracker = MusicTracker()
music_tracker.get_listened() # => []

'''
When we add a single track
It is reflected in the list of tracks
'''
music_tracker = MusicTracker()
music_tracker.add_music("Let it go, let it go...")
music_tracker.get_listened() # => ["Let it go, let it go..."]

'''
When we add multiple tracks
They are all reflected in the list of tracks
'''

music_tracker = MusicTracker()
music_tracker.add_music("Let it go, let it go...")
music_tracker.add_music("Wheel on the bus go round and round...")
music_tracker.get_listened() # => ["Let it go, let it go...", "Wheel on the bus go round and round..."]


'''
When we old music again
Then we raise an Exception
'''

music_tracker = MusicTracker()
music_tracker.add_music("Let it go, let it go...")
music_tracker.add_music("Wheel on the bus go round and round...")
music_tracker.get_listened() # => ["Let it go, let it go...", "Wheel on the bus go round and round..."]
music_tracker.add_music("Wheel on the bus go round and round...") #=> Raise an error "The song has already being tracked!"
music_tracker.get_listened() # => ["Let it go, let it go...", "Wheel on the bus go round and round..."]



## 4. Implementing the Behaviour
_After each test you write, follow the test driving process of red, green and refactor to implement the behaviour