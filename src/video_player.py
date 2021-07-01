"""A video player class."""

from src.video_library import VideoLibrary



class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.play = []
        self.playlist = []
        self.videolist = []
        self.co = 0

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        arr = self._video_library.get_all_videos()
        sep = ' '
        print("Here's a list of all available videos:")
        for i in range(len(arr)):
            print("  "+arr[i].title + " ("+arr[i].video_id+") "+"["+str(sep.join(arr[i].tags))+"]")
        # print("show_all_videos needs implementation")

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        arr = self._video_library.get_video(video_id)
        if arr is None:
            print("Cannot play video: Video does not exist")
            return
        if len(self.play) > 0:
            a = self.play.pop()
            print("Stopping video: "+a)
            self.play.append(arr.title)
        else:
            self.play.append(arr.title)
        print("Playing video: "+arr.title)
        self.co = 0


    def stop_video(self):
        """Stops the current video."""
        if len(self.play) > 0:
            a = self.play.pop()
            print("Stopping video: "+a)
            self.co = 0
        else:
            print("Cannot stop video: No video is currently playing")
        # print("stop_video needs implementation")

    def play_random_video(self):
        """Plays a random video from the video library."""

        from random import randint
        arr = self._video_library.get_all_videos()
        vid = []
        for i in range(len(arr)):
            vid.append(arr[i].title)
        a = randint(0, len(arr)-1)
        ch = vid[a]
        if len(self.play) > 0:
            p = self.play.pop()
            print("Stopping video: " + p)
            self.play.append(ch)
        else:
            self.play.append(ch)
        print("Playing video: " + ch)

        # print("play_random_video needs implementation")

    def pause_video(self):
        """Pauses the current video."""

        if len(self.play) > 0 and self.co == 0:
            print("Pausing video: "+self.play[0])
            self.co = 1
        elif len(self.play) > 0 and self.co > 0:
            print("Video already paused: "+self.play[0])
        else:
            print("Cannot pause video: No video is currently playing")



        # print("pause_video needs implementation")

    def continue_video(self):
        """Resumes playing the current video."""

        if self.co == 0 and len(self.play) > 0:
            print("Cannot continue video: Video is not paused")
        elif self.co > 0 and len(self.play) > 0:
            self.co = 0
            print("Continuing video: " + self.play[0])
        else:
            print("Cannot continue video: No video is currently playing")
        # print("continue_video needs implementation")

    def show_playing(self):
        """Displays video currently playing."""
        arr = self._video_library.get_all_videos()
        sep = ' '
        if len(self.play) > 0:
          for i in range(len(arr)):
            if self.play[0] == arr[i].title and self.co == 0:
                print("Currently playing: "+arr[i].title + " ("+arr[i].video_id+") "+"["+str(sep.join(arr[i].tags))+"]")
            elif self.play[0] == arr[i].title and self.co > 0:
                print("Currently playing: "+arr[i].title + " ("+arr[i].video_id+") "+"["+str(sep.join(arr[i].tags))+"] - PAUSED")
        else:
            print("No video is currently playing")



    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        flag = 0
        if len(self.playlist) > 0:
            for i in self.playlist:
                if playlist_name.lower() == i.lower():
                    print("Cannot create playlist: A playlist with the same name already exists")
                    flag = 1
            if flag == 0:
                print("Successfully created new playlist: "+playlist_name)
                self.playlist.append(playlist_name)
        else:
            print("Successfully created new playlist: "+playlist_name)
            self.playlist.append(playlist_name)


    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """

        pln = playlist_name.lower()
        video = self._video_library.get_video(video_id)

        if video.title in self.playlist:
            if video != None:
                if video.flagged == None:
                    if video in self.playlist[pln]:
                        print("Cannot add video to " + playlist_name + ": Video already added")
                    else:
                        self.playlist[pln].append(video)
                        print("Added video to " + playlist_name + ":", video.title)
                else:
                    print("Cannot add video to " + playlist_name + ": Video is currently flagged (reason: " + \
                          video.flagged + ")")
            else:
                print("Cannot add video to " + playlist_name + ": Video does not exist")

        else:
            print("Cannot add video to " + playlist_name + ": Playlist does not exist")


        # print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
