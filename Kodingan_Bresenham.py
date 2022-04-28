#Nama 		: Nisa Amalia
#NIM 		: 20051397038
#Kelas 		: 2020 B
#Prodi 		: D4 Manajemen Informatika
#Matkul     : Grafika Komputer

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def MenggambarGarisMenggunakanBresenham(x1,x2,y1,y2):
    #menghitung nilai dX dan dY
    dX = abs(x2-x1)
    dY = abs(y2-y1)

    #hitung nilai p
    p = 2*dY-dX
    duadY = 2*dY
    duadYdX = 2*(dY-dX)

    #Menghitung nilai Langkah
    langkah = 0
    if(abs(dX)>abs(dY)):
        langkah = abs(dX)
    else:
        langkah = abs(dY)

    #Memulai menggambar menggunakan Bresenham
    #Membersihkan window
    glClear(GL_COLOR_BUFFER_BIT)
    #Menentukan warna
    glColor3f(1.0,0.0,0.0)
    #Spesifikasikan diameter dari pixel yang akan digammbar
    glPointSize(10.0)
    #Memilih mode point
    glBegin(GL_POINTS)

    #looping untuk menggambar titik-titik 
    while (x < xend):
        x = x+1
            if (p < 0):
                p += duadY
            else:
            if (y1 > y2):
                y = y-1
            else:
                y = y+1
                p += duadYdX
    glVertex2f(x, y)
    glEnd()
    glFlush()

def main():
    x1 = int(10)
    y1 = int(10)
    x2 = int(500)
    y2 = int(400)

    #inisialisasi glut
    glutInit(sys.argv)
    #inisialisasi tipe display glut
    glutInitDisplayMode(GLUT_RGB)
    #inisialisasi ukuran layar glut
    glutInitWindowSize(500,500)
    #inisiasliasi posisi layar glut
    glutInitWindowPosition(0,0)
    #inisialisasi pembuatan window
    glutCreateWindow("Algoritma Bresenham")
    glutDisplayFunc(lambda: MenggambarGarisMenggunakanBresenham(x1,y1,x2,y2))
    glutIdleFunc(lambda: MenggambarGarisMenggunakanBresenham(x1,y1,x2,y2))
    
    #Set warna background
    glClearColor(0.0,0.0,0.0,0.0)
    #Set warna titik
    glColor3f(6.0, .0, 6.0)
    #Set ukuran titik
    glPointSize(2.0)
    #Set ukuran look window
    gluOrtho2D(0.0, 800.0, 0.0, 600.0)
    glutMainLoop()

main()