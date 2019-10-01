from OpenGL.GL import *
from OpenGL.GLU import *
from .cube import Cube
import random


class RubixCube():
	def __init__(self, offset_x=0, offset_y=0, offset_z=0):
		self.raindow = False
		self.color = (1, 1, 1, 1)
		self.cubes = [
			[[], [], []],
			[[], [], []],
			[[], [], []],
		]
		for x in range(3):
			for y in range(3):
				for z in range(3):
					self.cubes[x][y].append(Cube(x, y, z))

	def wireframe(self):
		for x in range(3):
			for y in range(3):
				for z in range(3):
					if self.raindow:
						self.color = (random.random(), random.random(), random.random(), 1)
					self.cubes[x][y][z].set_color(self.color)
					self.cubes[x][y][z].wireframe()

	def fill(self):
		for x in range(3):
			for y in range(3):
				for z in range(3):
					if self.raindow:
						self.color = (random.random(), random.random(), random.random(), 1)
					self.cubes[x][y][z].set_color(self.color)
					self.cubes[x][y][z].fill()

	def set_color(self, color):
		self.color = color

	def toggle_rainbow(self):
		self.raindow = True
