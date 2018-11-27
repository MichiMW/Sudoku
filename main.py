import os
import sys
from constraint import Row, Column, smallbox, value, individual
from utils import convertBase9


def parseFile(filename):
  open_file = open(filename)
  content = open_file.readlines()
  encodedLine = ""
  for line in content:
    if "_" in line:
        encodedLine += ''.join(line.split())
  return encodedLine

def genGrid(string):
  arr = [[0 for x in range(9)] for x in range(9)]
  for i in range(9):
    for j in range(9):
      arr[i][j] = string[ i * 9 + j ]
  return arr

line = parseFile(sys.argv[1])
grid = genGrid(line)

clauses = 0
f = open('tempOutput.txt', 'w')
clauses += value(f, grid)
clauses += individual(f, grid)
clauses += Column(f, grid)
clauses += Row(f, grid)
clauses += smallbox(f, grid)
f.close()

f = open('tempOutput.txt','r')
temp = f.read()
f.close()

f = open('tempOutput.txt', 'w')
f.write("p cnf 729 " + str(clauses) + "\n")

f.write(temp)
f.close()

cmd = './riss tempOutput.txt SATOutput.txt'
os.system(cmd)

f = open('SATOutput.txt','r')
sat = f.readline().strip()

open_file = open("SolvedPuzzle.txt", 'w')

if(sat == 's SATISFIABLE'):
  numbers = f.readline().replace("v ", "")
  asArr = numbers.split(' ')
  open_file.write("experiment: generator (Time: " + " )" +"\n")
  open_file.write("number of tasks: 1" + "\n")
  open_file.write("task: 1" + "\n")
  open_file.write("puzzle size: " + "x" + " \n")

  for i in range(len(asArr)):
    asArr[i] = int(asArr[i])

  for y in range(9):
    line = ''
    for x in range(9):
      for z in range(9):
        if(asArr[y*81 + 9*x + z] >= 0):
          line = line + str(z + 1) + ' '
          break
    open_file.write(line + '\n')
else:
  print('\nProblem is unsatisfiable.')
  open_file.write("'\nProblem is unsatisfiable.'")
open_file.write('\n\n')
open_file.close()
