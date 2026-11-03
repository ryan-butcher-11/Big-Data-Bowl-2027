# ========================================
# Here we define parameters that we will apply
# to our data for this project. We store them
# here so that we have one consistent place
# to record what filters we're applying to our
# data in this WR Separation Analysis
# ========================================

# We are wanting to examine Wide Receivers
POSITION_OF_INTEREST = "WR"

# We want to examine 2023 rookies because those are
# the players that we have BDB26 data for
DRAFT_YEAR_OF_INTEREST = 2023

# When identifying the defenders of our players
# of interest, we want to consider DBs
DEF_POSITION_OF_INTEREST = ["CB", "FS", "SS"]

# We only want to consider man coverage situations
COVERAGE_OF_INTEREST = "MAN_COVERAGE"

# We want every player-play we examine to be at least
# 1.2 seconds long
MIN_PLAY_LENGTH_SECS = 1.2

# We don't want to include plays in red zone where team
# is close to scoring
ABSOLUTE_YARDLINE_BOUNDARY = [10, 90]
# FIFTY_YARD_YARDLINE_BOUNDARY = [20, 50]

# We only want to examine players who have sufficient
# exposure, we'll consider sufficient exposure to be
# 10 player-plays
MIN_NUM_PLAYER_PLAYS = 10
