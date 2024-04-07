import os
from productor import Productor

from .animal import Animal

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
start_dir = os.path.join(os.path.dirname(__file__))
animal_productor = Productor(root_dir, start_dir, Animal, None)

animal_class = animal_productor.random()()
