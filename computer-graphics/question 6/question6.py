
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_line(x1, y1, x2, y2):
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)  # Red color
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()
    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"Line Drawing")
    glClearColor(1.0, 1.0, 1.0, 1.0)  # White background
    glutDisplayFunc(lambda: draw_line(-0.5, -0.5, 0.5, 0.5))
    glutMainLoop()
