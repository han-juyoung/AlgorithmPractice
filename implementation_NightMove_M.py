# now = input()
# col = now[0]
# row = now[1]

# if col == 'a':
#   col = 1

# if col == 'b':
#   col = 2

# if col == 'c':
#   col = 3

# if col == 'd':
#   col = 4

# if col == 'e':
#   col = 5

# if col == 'f':
#   col = 6

# if col == 'g':
#   col = 7

# if col == 'h':
#   col = 8

# count = 0

# x, y = int(col), int(row)

# move = ['rd', 'ld', 'ru', 'lu', 'ur'
#         'ul'
#         'dr', 'dl']
# dx = [1, 1, -1, -1, -2, -2, 2, 2]
# dy = [2, -2, 2, -2, 1, -1, 1, -1]

# for i in range(len(move)):
#   if True:
#     move[i]
#     nx = x + dx[i]
#     ny = y + dy[i]
#     count += 1
#     if x < 1 or y < 1 or x > 8 or y > 8:
#       continue

# print(count)

now = input()
col = now[0]
row = int(now[1])
col = int(ord(col)) - int(ord('a')) + 1

move = [(1, 2), (1, -2), (-1, 2), (-1, -2), (-2, 1), (-2, -1), (2, 1), (2, -1)]
count = 0

for i in move:
  nrow = row + i[0]
  ncol = col + i[1]
  if nrow >= 1 and nrow <= 8 and ncol >= 1 and ncol <= 8:
    count += 1

print(count)
