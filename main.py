x="hello"
def reverse1(v,x):
  if v==-1:
    return ""
  return  x[v] + reverse1(v-1,x)
print(x)
print(reverse1(len(x)-1,x))