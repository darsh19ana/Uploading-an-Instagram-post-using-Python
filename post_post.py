from instagrapi import Client
from instagrapi.types import Usertag,Location
import configuration

cl = Client()
cl.login(configuration.username,configuration.password)

user = cl.user_info_by_username("darshhie")

media = cl.photo_upload (
    path = "C:\\Users\\darsh\\OneDrive\\Pictures\\serenn.jpg",
    caption= "serendipity",
    usertags=[Usertag(user=user, x=0.5,y=0.5)]
)