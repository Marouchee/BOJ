import sys
input = sys.stdin.readline

n=int(input())

tree=dict()

for _ in range(n):
  x,y,z=map(str, input().split())
  tree[x]=[y,z]

def preorder(k):
  if k != '.':
    print(k, end='')
    preorder(tree[k][0])
    preorder(tree[k][1])

def inorder(k):
  if k != '.':
    inorder(tree[k][0])
    print(k, end='')
    inorder(tree[k][1])

def postorder(k):
  if k != '.':
    postorder(tree[k][0])
    postorder(tree[k][1])
    print(k, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')
