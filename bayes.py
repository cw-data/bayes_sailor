import sys
import random
import itertools
import numpy as np
import cv2 as cv
import search
from importlib import reload
reload(search)

MAP_FILE = 'cape_python.png'

"""Establish search area boxes"""
SA1_CORNERS = (130, 265, 180, 315)
SA2_CORNERS = (80, 255, 130, 305)
SA3_CORNERS = (105, 205, 155, 255)

'''Some code to test that search.Search() works properly'''
mysearch = search.Search(
    name="myname",
    map_file=MAP_FILE,
    SA1_CORNERS=SA1_CORNERS,
    SA2_CORNERS=SA2_CORNERS,
    SA3_CORNERS=SA3_CORNERS
    )
mysearch.describe_search()

