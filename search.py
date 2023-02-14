"""A module to be used in bayes.py"""
import cv2 as cv
import sys

class Search():
    '''A class Search'''

    def __init__(self, name, map_file, SA1_CORNERS, SA2_CORNERS, SA3_CORNERS):
        '''Constructor method for class Search'''
        self.name = name
        self.map_file = map_file
        self.img = cv.imread(self.map_file, cv.IMREAD_COLOR)
        if self.img is None:
            print(
                'Could not load map file {}'.format(self.map_file),
                file=stderr
            )
            sys.exit(1)
        self.SA1_CORNERS = SA1_CORNERS
        self.SA2_CORNERS = SA2_CORNERS
        self.SA3_CORNERS = SA3_CORNERS
        self.area_actual = 0
        self.sailor_actual = [0, 0] # local coords within search area for the sailor

        self.sa1 = self.img[
            self.SA1_CORNERS[1] : self.SA1_CORNERS[3],
            self.SA1_CORNERS[0] : self.SA1_CORNERS[2]
        ]

        self.sa2 = self.img[
            self.SA2_CORNERS[1] : self.SA2_CORNERS[3],
            self.SA2_CORNERS[0] : self.SA2_CORNERS[2]
        ]

        self.sa3 = self.img[
            self.SA3_CORNERS[1] : self.SA3_CORNERS[3],
            self.SA3_CORNERS[0] : self.SA3_CORNERS[2]
        ]

        self.p1 = 0.2
        self.p2 = 0.5
        self.p3 = 0.3

        self.sep1 = 0
        self.sep2 = 0
        self.sep3 = 0

    def describe_search(self):
        '''A method to test that class Search is constructed properly'''
        print(f"The name is {self.name}")
        print(f"The image is {self.img}")
