import webbrowser  # Import this module to open webpages in the code


class Movie():
    """
    Class Movie holds all the necessary information
    like Movie's title, storyline, poster and trailer url.
    """
    def __init__(self, title, storyline, poster, trailer_link):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer_link

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
