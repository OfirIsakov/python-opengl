from OpenGL.GL import *
from OpenGL.GLU import *
from objects import *
import glfw
import time
import random


WIDTH = 800
HEIGHT = 600
FPS = 300

verticies = (
	( 1, -1, -1),
	( 1,  1, -1),
	(-1,  1, -1),
	(-1, -1, -1),
	( 1, -1,  1),
	( 1,  1,  1),
	(-1, -1,  1),
	(-1,  1,  1)
)

edges = (
	(0, 1),
	(0, 3),
	(0, 4),
	(2, 1),
	(2, 3),
	(2, 7),
	(6, 3),
	(6, 4),
	(6, 7),
	(5, 1),
	(5, 4),
	(5, 7)
)

surfaces = (
	(0, 1, 2, 3),
	(3, 2, 7, 6),
	(6, 7, 5, 4),
	(4, 5, 1, 0),
	(1, 5, 7, 2),
	(4, 0, 3, 6),
)


def cube_wireframe(offset=0):
	glBegin(GL_LINES)

	for edge in edges:
		for vertex in edge:
			glVertex3f(
				verticies[vertex][0] + offset,
				verticies[vertex][1] + offset,
				verticies[vertex][2] + offset,
			)

	glEnd()


def cube_full(offset=0):
	glBegin(GL_QUADS)
	i = 0
	for surface in surfaces:
		i += 1
		glColor4fv((random.random(), random.random(), random.random(), 1.0))
		for vertex in surface:
			glVertex3f(
				verticies[vertex][0] + offset,
				verticies[vertex][1] + offset,
				verticies[vertex][2] + offset,
			)

	glEnd()


def make_window():
	pass


def main():
	if not glfw.init():
		return

	display = glfw.create_window(WIDTH, HEIGHT, "Ofir's OpenGL Graphics", None, None)

	if not display:
		glfw.terminate()
		return

	glfw.set_key_callback(display, key_handler)

	glfw.set_input_mode(display, glfw.CURSOR, glfw.CURSOR_HIDDEN)
	glfw.set_cursor_pos_callback(display, mouse_move_handler)

	glfw.set_mouse_button_callback(display, key_click_handler)

	glfw.make_context_current(display)

	gluPerspective(45, (WIDTH / HEIGHT), 0.1, 50.0)

	glTranslatef(0.0, 0.0, -10.0)

	pyramid = Pyramid(0, 1, 0, 3)
	# cube2.toggle_rainbow()
	pyramid.set_color((1, 1, 1, 1))
	# cube2.set_color((0, 1, 0, 1))
	while not glfw.window_should_close(display):
		glfw.poll_events()

		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

		# glRotatef(2, 1, 2, 1)
		pyramid.fill()

		glfw.swap_buffers(display)
		time.sleep(1 / FPS)

	glfw.terminate()


def key_handler(display, key, scan_code, action, mods):
	key = ord(chr(key).lower())
	print(key)
	if not action == 0:
		if key == ord('w'):
			glTranslatef(0.0, 0.0, 0.1)
		if key == ord('a'):
			glTranslatef(0.1, 0.0, 0.0)
		if key == ord('s'):
			glTranslatef(0.0, 0.0, -0.1)
		if key == ord('d'):
			glTranslatef(-0.1, 0.0, 0.0)
		if key == 32:
			glTranslatef(0.0, -0.1, 0.0)
		if key == 341:
			glTranslatef(0.0, 0.1, 0.0)
		if key == 257:  # If "esc" pressed
			exit()


def key_click_handler(display, button, action, mods):
	print((button, action, mods))


def mouse_move_handler(display, x, y):
	print((x, y))
	glfw.set_cursor_pos(display, WIDTH // 2, HEIGHT // 2)
	# glRotatef(0.1, 0.0, 1.0, 0.0)
	if WIDTH // 2 > x:
		glRotatef(1, 0, 1, 0)
	if WIDTH // 2 < x:
		glRotatef(1, 0, -1, 0)


if __name__ == "__main__":
	main()
