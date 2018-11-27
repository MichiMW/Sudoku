from utils import convertBase9

def Row(f, grid):
  count = 0
  for y in range(1, 10):
    for z in range(1, 10):
      for x in range(1, 9):
        for i in range(x + 1, 10):
          f.write("-" + str(convertBase9(x, y, z)) + " -" +  str(convertBase9(i, y, z)) + " 0\n")
          count += 1
  return count

def Column(f, grid):
  count = 0
  for x in range(1,10):
    for z in range(1, 10):
      for y in range(1,9):
        for i in range(y + 1, 10):
          f.write("-" + str(convertBase9(x, y, z)) + " -" + str(convertBase9(x, i, z)) + " 0\n")
          count += 1
  return count

def smallbox(f, grid):
  count = 0
  for z in range(1, 10):
    for gridX in range(0, 3):
      for gridY in range(0, 3):
        for x in range(1, 4):
          for y in range(1, 4):

            for k in range(y + 1, 4):
              a = gridX * 3 + x
              b = gridY * 3 + y
              c = gridY * 3 + k
              f.write('-' + str(convertBase9(a,b,z)) + ' -' + str(convertBase9(a,c,z)) + ' 0\n')
              count += 1

            for k in range (x + 1, 4):
              for l in range(1, 4):
                a = gridX * 3 + x
                b = gridY * 3 + y
                c = gridX * 3 + k
                d = gridY * 3 + l
                f.write('-' +  str(convertBase9(a,b,z)) + ' -' + str(convertBase9(c,d,z)) + ' 0\n')
                count += 1
  return count

def value(f, grid):
  count = 0
  for x in range(9):
    for y in range(9):
      if grid[x][y] == int():
        f.write(str(convertBase9(x+1, y+1, int(grid[x][y]))) + ' 0\n')
        count += 1
  return count

def individual(f, grid):
  count = 0
  for x in range(1, 10):
    for y in range(1, 10):
      for z in range(1, 10):
        f.write(str(convertBase9(x, y, z))+' ')
      f.write(' 0\n')
      count += 1
  return count
