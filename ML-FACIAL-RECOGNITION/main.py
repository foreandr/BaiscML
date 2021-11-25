import face_recognition
import os
import cv2
from PIL import Image

# CONSTANTS
KNOWN_FACES_DIR = 'known-faces'
UNKOWN_FACES_DIR = 'unkown-faces'
TOLERANCE = 0.6  # FOR FALSE POSITIVES # HIGHER = MORE FALSE POSIITVES
