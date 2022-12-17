#Maria Bruna Pilotto - 12560085
#Mariana Tavares Mozini - 12560151
#Calculo da rotacao entre dois planos (Euler Angle)

#Importando bibliotecas utilizadas
import math
import numpy as np
import matplotlib.pyplot as plt

#Calcular a rotacao entre dois planos
def rot_plano(p1, p2):
    #Vetor normal ao plano 1
    n_p1 = np.cross(p1[0], p1[1])
    n_p1 = n_p1 / np.linalg.norm(n_p1)
    #Vetor normal ao plano 2
    n_p2 = np.cross(p2[0], p2[1])
    n_p2 = n_p2 / np.linalg.norm(n_p2)
    #Outros parametros que vamos utilizar
    v = np.cross(n_p1, n_p2)
    c = np.dot(n_p1, n_p2)
    s = np.linalg.norm(v)
    k = np.array([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])
    #Calculo da Rotacao
    rot = np.eye(3) + k + np.dot(k, k) * ((1 - c) / (s ** 2))
    return rot

#Calcular o angulo de rotação entre dois planos
def angulo_rot(p1, p2):
    #Vetor normal ao plano 1
    n_p1 = np.cross(p1[0], p1[1])
    n_p1 = n_p1 / np.linalg.norm(n_p1)
    #Vetor normal ao plano 2
    n_p2 = np.cross(p2[0], p2[1])
    n_p2 = n_p2 / np.linalg.norm(n_p2)
    #Outros parametros que vamos utilizar
    v = np.cross(n_p1, n_p2)
    c = np.dot(n_p1, n_p2)
    s = np.linalg.norm(v)
    #Calculo do angulo de rotacao
    angulo = math.atan_p2(s, c)
    return angulo

#Funcao que recebebe os dados e calcula a rotacao e o angulo de rotacao
def final(dados):
    #Rotacao entre os planos
    rot = rot_plano(dados[0], dados[1])
    #Angulo de rotacao entre os planos
    angulo = angulo_rot(dados[0], dados[1])
    angulo = math.degrees(angulo)
    angulo = round(angulo, 2)
    return rot, angulo

#Plotar os dados de rotacao
def plot_dados(dados, angulo):
    rot, angulo = final(dados)
    print(rot)
    print(angulo)
    plt.figure()
    plt.plot(dados[0][0], dados[0][1], 'r')
    plt.plot(dados[1][0], dados[1][1], 'b')
    plt.show()

#Visualizar dados
def visualiza(x,y,z, planox, planoy, planoz):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z, c='r', marker='o')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xlim(planox)
    ax.set_ylim(planoy)
    ax.set_zlim(planoz)
    plt.show()

visualiza(x,y,z, (-10,10), (-10,10), (-10,10))

#Visualiza planos cruzados 3D
def visualiza(x,y,z, planox, planoy, planoz):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z, c='r', marker='o')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xlim(planox)
    ax.set_ylim(planoy)
    ax.set_zlim(planoz)
    plt.show()

visualiza(x,y,z, (-10,10), (-10,10), (-10,10))