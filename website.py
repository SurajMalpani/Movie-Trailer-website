import media   # import media.py file to access the class Movie definitions
import fresh_tomatoes  # import fresh_tomatoes.py file to generate webpage

argo = media.Movie("Argo",
                   "Acting under the cover of a Hollywood producer scouting a "
                   "location for a science fiction film, a CIA agent launches "
                   "a dangerous operation to rescue six Americans in Tehran "
                   "during the U.S. hostage crisis in Iran in 1980.",
                   "https://upload.wikimedia.org/wikipedia/en/e/e1/Argo2012Poster.jpg",  # NOQA
                   "https://www.youtube.com/watch?v=JW3WfSFgrVY")

before_sunrise = media.Movie("Before Sunrise",
                            "While travelling on a train in Europe, Jesse,"
                            " meets Celine On his last day in Europe before"
                            " returning to the US, he decides to spend"
                            " his remaining hours with her.",
                            "http://t0.gstatic.com/images?q=tbn:ANd9GcR1P-mPnVeKEZbHA_p0gC0osmQqYhHCOGeXcQDIeqkd0xevmmSW",  # NOQA
                            "https://www.youtube.com/watch?v=25v7N34d5HE")

seven_pounds = media.Movie("Seven Pounds",
                           "Ben Thomas, an IRS agent,"
                           " embarks on an extraordinary journey in order to "
                           "change the lives of seven strangers.",
                           "http://www.gstatic.com/tv/thumb/movieposters/175217/p175217_p_v8_af.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=hvu2F6t26hs")

stuck_in_love = media.Movie("Stuck in Love",
                            "A successful writer (Greg Kinnear) tries to "
                            "reconnect with his two children "
                            "(Lily Collins, Nat Wolff) after his divorce.",
                            "http://www.gstatic.com/tv/thumb/movieposters/9816875/p9816875_p_v8_aa.jpg",  # NOQA
                            "https://www.youtube.com/watch?v=ORKb_Vqbz9U")

k_pax = media.Movie("K-PAX",
                    "Robert, a mentally unstable man,"
                    " tries to convince the hospital staff that he is from "
                    "a planet called K-PAX.",
                    "http://www.gstatic.com/tv/thumb/movieposters/28596/p28596_p_v8_ae.jpg",  # NOQA
                    "https://www.youtube.com/watch?v=bVfHNhBcMTw")

interstellar = media.Movie("Interstellar",
                            "In the future, Earth is becoming uninhabitable. "
                            "Ex-NASA pilot Cooper, along with a team,"
                            " is sent on a planet exploration mission to "
                            "report which planet can sustain life.",
                            "http://t1.gstatic.com/images?q=tbn:ANd9GcRf61mker2o4KH3CbVE7Zw5B1-VogMH8LfZHEaq3UdCMLxARZAB",  # NOQA
                            "https://www.youtube.com/watch?v=zSWdZVtXT7E")

movies = [argo, before_sunrise, interstellar, seven_pounds,
          k_pax, stuck_in_love]
fresh_tomatoes.open_movies_page(movies)
