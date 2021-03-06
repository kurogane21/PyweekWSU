"""This is the entry point to the game. It initializes cocos2d, creates the game window and launches the initial game scene.
"""
import cocos
from cocos.director import director
import mainmenu

# Initialize game window
director.init()

# Simply start up the game with our main menu scene.
# If we get far enough we should have a fancy intro scene that comes before the main menu.
director.run(mainmenu.get_scene())
