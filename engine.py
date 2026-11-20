import json,os,urllib.request as U
E=os.environ['MAKEFUN_ENV_URL']
def post(r,o):return json.load(U.urlopen(U.Request(E+r,json.dumps(o).encode(),{'content-type':'application/json'})))
# PeSTO piece-square tables (Ronald Friederich, via the Chess Programming Wiki), mg then eg for P N B R Q K,
# a8..h1 for white, each value v stored as chr(v//2+180)
V=[82,337,365,477,1025,30000,94,281,297,512,936,30000]
S=''.join(chr(v//2+180)for v in(
0,0,0,0,0,0,0,0,98,134,61,95,68,126,34,-11,-6,7,26,31,65,56,25,-20,-14,13,6,21,23,12,17,-23,-27,-2,-5,12,17,6,10,-25,-26,-4,-4,-10,3,3,33,-12,-35,-1,-20,-23,-15,24,38,-22,0,0,0,0,0,0,0,0,
-167,-89,-34,-49,61,-97,-15,-107,-73,-41,72,36,23,62,7,-17,-47,60,37,65,84,129,73,44,-9,17,19,53,37,69,18,22,-13,4,16,13,28,19,21,-8,-23,-9,12,10,19,17,25,-16,-29,-53,-12,-3,-1,18,-14,-19,-105,-21,-58,-33,-17,-28,-19,-23,
-29,4,-82,-37,-25,-42,7,-8,-26,16,-18,-13,30,59,18,-47,-16,37,43,40,35,50,37,-2,-4,5,19,50,37,37,7,-2,-6,13,13,26,34,12,10,4,0,15,15,15,14,27,18,10,4,15,16,0,7,21,33,1,-33,-3,-14,-21,-13,-12,-39,-21,
32,42,32,51,63,9,31,43,27,32,58,62,80,67,26,44,-5,19,26,36,17,45,61,16,-24,-11,7,26,24,35,-8,-20,-36,-26,-12,-1,9,-7,6,-23,-45,-25,-16,-17,3,0,-5,-33,-44,-16,-20,-9,-1,11,-6,-71,-19,-13,1,17,16,7,-37,-26,
-28,0,29,12,59,44,43,45,-24,-39,-5,1,-16,57,28,54,-13,-17,7,8,29,56,47,57,-27,-27,-16,-16,-1,17,-2,1,-9,-26,-9,-10,-2,-4,3,-3,-14,2,-11,-2,-5,2,14,5,-35,-8,11,2,8,15,-3,1,-1,-18,-9,10,-15,-25,-31,-50,
-65,23,16,-15,-56,-34,2,13,29,-1,-20,-7,-8,-4,-38,-29,-9,24,2,-16,-20,6,22,-22,-17,-20,-12,-27,-30,-25,-14,-36,-49,-1,-27,-39,-46,-44,-33,-51,-14,-14,-22,-46,-44,-30,-15,-27,1,7,-8,-64,-43,-16,9,8,-15,36,12,-54,8,-28,24,14,
0,0,0,0,0,0,0,0,178,173,158,134,147,132,165,187,94,100,85,67,56,53,82,84,32,24,13,5,-2,4,17,17,13,9,-3,-7,-7,-8,3,-1,4,7,-6,1,0,-5,-1,-8,13,8,8,10,13,0,2,-7,0,0,0,0,0,0,0,0,
-58,-38,-13,-28,-31,-27,-63,-99,-25,-8,-25,-2,-9,-25,-24,-52,-24,-20,10,9,-1,-9,-19,-41,-17,3,22,22,22,11,8,-18,-18,-6,16,25,16,17,4,-18,-23,-3,-1,15,10,-3,-20,-22,-42,-20,-10,-5,-2,-20,-23,-44,-29,-51,-23,-15,-22,-18,-50,-64,
-14,-21,-11,-8,-7,-9,-17,-24,-8,-4,7,-12,-3,-13,-4,-14,2,-8,0,-1,-2,6,0,4,-3,9,12,9,14,10,3,2,-6,3,13,19,7,10,-3,-9,-12,-3,8,10,13,3,-7,-15,-14,-18,-7,-1,4,-9,-15,-27,-23,-9,-23,-5,-9,-16,-5,-17,
13,10,18,15,12,12,8,5,11,13,13,11,-3,3,8,3,7,7,7,5,4,-3,-5,-3,4,3,13,1,2,1,-1,2,3,5,8,4,-5,-6,-8,-11,-4,0,-5,-1,-7,-12,-8,-16,-6,-6,0,2,-9,-9,-11,-3,-9,2,3,-1,-5,-13,4,-20,
-9,22,22,27,27,19,10,20,-17,20,32,41,58,25,30,0,-20,6,9,49,47,35,19,9,3,22,24,45,57,40,57,36,-18,28,19,47,31,34,39,23,-16,-27,15,6,9,17,10,5,-22,-23,-30,-16,-16,-23,-36,-32,-33,-28,-22,-43,-5,-32,-20,-41,
-74,-35,-18,-18,-11,15,4,-17,-12,17,14,17,17,38,23,11,10,17,23,15,20,45,44,13,-8,22,24,27,26,33,26,3,-18,-4,21,24,27,23,9,-11,-19,-3,11,21,23,16,7,-9,-27,-11,4,13,14,4,-5,-17,-53,-34,-21,-11,-28,-24,-14,-43))
D={'P':(-10,-20,-11,-9),'N':(-19,-8,12,21,19,8,-12,-21),'B':(-11,-9,9,11),'R':(-10,1,10,-1)}
D['Q']=D['K']=D['B']+D['R']
M,L=99999,20000
def tables(b):
 # blend mg/eg by the root's phase; P[0] for white to move, P[1] (files mirrored) for black
 ph=min(24,sum(b.count(x)*w for x,w in zip('NBRQnbrq',(1,1,2,4)*2)))
 P=[{},{}]
 for k,x in enumerate('PNBRQK'):
  for c in 0,1:
   t=[0]*120
   for r in range(1,9):
    for f in range(8):
     s=(8-r)*8+(f if c==0 else 7-f)
     t[101+f-10*r]=((V[k]+ord(S[k*64+s])*2-360)*ph+(V[k+6]+ord(S[k*64+s+384])*2-360)*(24-ph))//24
   P[c][x]=t
 return P
def gen(p):
 b,s,wc,bc,ep,kp,c=p
 for i,x in enumerate(b):
  if x.isupper():
   for d in D[x]:
    j=i+d
    while 1:
     y=b[j]
     if y.isspace() or y.isupper():break
     if x=='P':
      if d in(-10,-20)and y!='.':break
      if d==-20 and(i<81 or b[i-10]!='.'):break
      if d in(-11,-9)and y=='.'and j not in(ep,kp,kp-1,kp+1):break
      if j<29:
       for q in'QNRB':yield i,j,q
       break
     yield i,j,''
     if x in'PNK'or y.islower():break
     if i==91 and b[j+1]=='K'and wc[0]:yield j+1,j-1,''
     if i==98 and b[j-1]=='K'and wc[1]:yield j-1,j+1,''
     j+=d
def val(p,m):
 b,s,wc,bc,ep,kp,c=p
 i,j,q=m
 x,y=b[i],b[j]
 T,O=P[c],P[1-c]
 v=T[x][j]-T[x][i]
 if y.islower():v+=O[y.upper()][119-j]
 if abs(j-kp)<2:v+=O['K'][119-j]
 if x=='K'and abs(j-i)==2:v+=T['R'][(i+j)//2]-T['R'][91 if j<i else 98]
 if x=='P':
  if j<29:v+=T[q][j]-T['P'][j]
  if j==ep:v+=O['P'][109-j]
 return v
def rot(p,n=0):
 b,s,wc,bc,ep,kp,c=p
 return b[::-1].swapcase(),-s,bc,wc,0 if n else 119-ep if ep else 0,0 if n else 119-kp if kp else 0,1-c
def mv(p,m):
 b,s,wc,bc,ep,kp,c=p
 i,j,q=m
 x=b[i]
 s+=val(p,m)
 b=b[:j]+x+b[j+1:]
 b=b[:i]+'.'+b[i+1:]
 ep=kp=0
 if i==91:wc=0,wc[1]
 if i==98:wc=wc[0],0
 if j==21:bc=bc[0],0
 if j==28:bc=0,bc[1]
 if x=='K':
  wc=0,0
  if abs(j-i)==2:
   kp=(i+j)//2
   r=91 if j<i else 98
   b=b[:r]+'.'+b[r+1:]
   b=b[:kp]+'R'+b[kp+1:]
 if x=='P':
  if j<29:b=b[:j]+q+b[j+1:]
  if j-i==-20:ep=i-10
  if j==p[4]:b=b[:j+10]+'.'+b[j+11:]
 return rot((b,s,wc,bc,ep,kp,c))
class Z(Exception):pass
def srch(p,a,b,d,h,nl=1):
 # negamax alpha-beta, fail-soft; d<=0 is the quiescence search
 global N
 N+=1
 if N>LIM:raise Z
 s=p[1]
 if s<-L:return h-M
 k=p[0]
 if k in R:return C if h%2 else -C
 e=T.get(p)
 tm=None
 if e:
  tm=e[3]
  if e[0]>=d:
   f,v=e[1],e[2]
   if f==0 or f>0 and v>=b or f<0 and v<=a:return v
 a0=a
 if d<=0:
  if s>=b:return s
  if s>a:a=s
  best=s;bm=None
  for v,m in sorted(((val(p,m),m)for m in gen(p)),reverse=True):
   if v<QL or s+v<=a:break
   x=-srch(mv(p,m),-b,-a,d-1,h+1)
   if x>best:best,bm=x,m
   if x>a:a=x
   if a>=b:break
 else:
  if nl and d>2 and s>=b and any(x in k for x in'NBRQ'):
   x=-srch(rot(p,1),-b,1-b,d-3,h+1,0)
   if x>=b:return x
  kl=K.get(h)
  ms=sorted(((val(p,m),m)for m in gen(p)),key=lambda o:o[0]+(M if o[1]==tm else 150 if o[1]==kl else 0),reverse=True)
  best=-M;bm=None;n=0
  R.add(k)
  for v,m in ms:
   if d==1 and n and s+v+60<=a:
    best=max(best,s+v);break
   c=mv(p,m)
   if n:
    r=d>2 and n>3 and v<60 and m!=kl
    x=-srch(c,-a-1,-a,d-1-r,h+1)
    if r and x>a:x=-srch(c,-a-1,-a,d-1,h+1)
    if a<x<b:x=-srch(c,-b,-a,d-1,h+1)
   else:x=-srch(c,-b,-a,d-1,h+1)
   n+=1
   if x>best:best,bm=x,m
   if x>a:a=x
   if a>=b:
    if v<60:K[h]=m
    break
  R.discard(k)
  if best<-L and d>1:
   q=rot(p,1)
   if all(val(q,m)<L for m in gen(q)):best=0
 T[p]=d,(best>=b)-(best<=a0),best,bm
 return best
def think(p,ms,lim):
 global N,LIM
 N=0;LIM=lim*2;bm=ms[0];d=1
 try:
  while N<lim/3 and d<40:
   e=T.get(p);tm=e and e[3]
   ms.sort(key=lambda m:m!=tm)
   a=-M;bb=None
   for m in ms:
    c=mv(p,m)
    if bb:
     x=-srch(c,-a-1,-a,d-1,1)
     if x>a:x=-srch(c,-M,-a,d-1,1)
    else:x=-srch(c,-M,-a,d-1,1)
    if x>a:a,bb=x,m;bm=m
   T[p]=d,0,a,bb
   d+=1
 except Z:pass
 return bm
def sq(u,c):
 i=101+ord(u[0])-97-10*int(u[1])
 return 119-i if c else i
def nm(i,c):
 if c:i=119-i
 return'abcdefgh'[i%10-1]+str(10-i//10)
I='         \n'*2+' rnbqkbnr\n pppppppp\n'+' ........\n'*4+' PPPPPPPP\n RNBQKBNR\n'+'         \n'*2
T={};K={};QL=150;LIM=0
while 1:
 g=post('/game',{})
 if g['status']=='done':break
 C=[60,50,40,20,0,0,0,0][g['game']-1]
 while g['status']=='your_move':
  P=tables(g['fen'])
  p=(I,0,(1,1),(1,1),0,0,0);R=set()
  for u in g['moves']:
   R.add(p[0]);c=p[6]
   p=mv(p,(sq(u[:2],c),sq(u[2:4],c),u[4:].upper()))
  b,c=p[0],p[6]
  p=(b,sum(P[c][x][i]if x.isupper()else-P[1-c][x.upper()][119-i]for i,x in enumerate(b)if x.isalpha()),)+p[2:]
  if len(T)>3e5:T.clear()
  m=think(p,[(sq(u[:2],c),sq(u[2:4],c),u[4:].upper())for u in g['legal_moves']],NB)
  g=post('/move',{'game':g['game'],'move':nm(m[0],c)+nm(m[1],c)+m[2].lower()})
