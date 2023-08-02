class MusicTracker:
    def __init__(self):
        self._musicTrack = []

    def add_music(self, track):
        if track in self._musicTrack:
            raise Exception("The song has already being tracked!")
        self._musicTrack.append(track)

    def get_listened(self):
        return self._musicTrack