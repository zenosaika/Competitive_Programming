# https://www.borntodev.com/devlab/task/860

n = int(input())
l = ['0'] * (n*2+1)
r = []
for i in range(n+1):
  for j in range(i, n*2+1-i):
    l[j] = str(i)
  r.append(''.join(l))
  
r += r[::-1][1:]
print('\n'.join(r))
    