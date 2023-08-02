from lib.music_tracker import MusicTracker
import pytest
'''
python
Initially, there are no music added
'''
def test_no_music_added():
    music_tracker = MusicTracker()
    assert music_tracker.get_listened() == []

'''
When we add a single track
It is reflected in the list of tracks
'''
def test_add_single_music():
    music_tracker = MusicTracker()
    music_tracker.add_music("Let it go, let it go...")
    assert music_tracker.get_listened() == ["Let it go, let it go..."]

'''
When we add multiple tracks
They are all reflected in the list of tracks
'''
def test_add_multiple_tracks():
    music_tracker = MusicTracker()
    music_tracker.add_music("Let it go, let it go...")
    music_tracker.add_music("Wheel on the bus go round and round...")
    assert music_tracker.get_listened() == ["Let it go, let it go...", "Wheel on the bus go round and round..."]

'''
When we add old music again
Then we raise an Exception
'''
def test_add_old_music_and_get_error():
    music_tracker = MusicTracker()
    music_tracker.add_music("Let it go, let it go...")
    music_tracker.add_music("Wheel on the bus go round and round...")
    music_tracker.get_listened() # => ["Let it go, let it go...", "Wheel on the bus go round and round..."]
    with pytest.raises (Exception) as e:
        music_tracker.add_music("Wheel on the bus go round and round...") #=> Raise an error "The song has already being tracked!"
    assert str(e.value) == "The song has already being tracked!"
    
    music_tracker.get_listened() # => ["Let it go, let it go...", "Wheel on the bus go round and round..."]