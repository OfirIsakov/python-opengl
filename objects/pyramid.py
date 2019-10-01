from OpenGL.GL import *
from OpenGL.GLU import *
import itertools


class Pyramid():
	def __init__(self, offset_x=0, offset_y=0, offset_z=0, size=1):
		self.offset_x = offset_x
		self.offset_y = offset_y
		self.offset_z = offset_z

		self.verticies = (
			(-0.5 * size, -0.5 * size, -0.5 * size),
			( 0.5 * size, -0.5 * size, -0.5 * size),
			( 0.5 * size, -0.5 * size,  0.5 * size),
			(-0.5 * size, -0.5 * size,  0.5 * size),
			( 0.0 * size,  0.5 * size,  0.0 * size),
		)
		self.edges = (
			(0, 1),
			(0, 3),
			(2, 1),
			(2, 3),
			(4, 0),
			(4, 1),
			(4, 2),
			(4, 3),
		)
		self.surfaces = (
			(0, 1, 2, 3),
			(0, 1, 4),
			(0, 3, 4),
			(2, 1, 4),
			(2, 3, 4),
		)
		self.color = (1, 1, 1, 1)

	def wireframe(self):
		glBegin(GL_LINES)

		for edge in self.edges:
			glColor4fv(self.color)
			for vertex in edge:
				glVertex3f(
					self.verticies[vertex][0] + self.offset_x,
					self.verticies[vertex][1] + self.offset_y,
					self.verticies[vertex][2] + self.offset_z,
				)

		glEnd()

	def fill(self):
		for surface in self.surfaces:
			print(surface)
			glBegin(GL_QUADS)
			glColor4fv(self.color)

			for vertex in surface:
				glVertex3f(
					self.verticies[vertex][0] + self.offset_x,
					self.verticies[vertex][1] + self.offset_y,
					self.verticies[vertex][2] + self.offset_z,
				)

			glEnd()

			self.invert_color()
			glBegin(GL_LINES)
			glColor4fv(self.color)

			edges = itertools.combinations(surface, 2)

			for edge in edges:
				for verte in edge:
					glVertex3f(
						self.verticies[verte][0] + self.offset_x,
						self.verticies[verte][1] + self.offset_y,
						self.verticies[verte][2] + self.offset_z,
					)

			glEnd()
			self.invert_color()

	def set_color(self, color):
		self.color = color

	def invert_color(self):
		new_color = []
		for i in range(3):
			new_color.append(1 - self.color[i])
		new_color.append(1)
		self.color = tuple(new_color)
