# https://wsdookadr.github.io/posts/p9/

# o,y,p,b,g
# o: orange
# y: yellow
# p: pink
# b: blue
# g: green
# w: width
# h: height

from sympy import *
ow,oh,yw,yh,pw,ph,bw,bh,gw,gh = symbols('o_w o_h y_w y_h p_w p_h b_w b_h g_w g_h')
u1 = ow+bw
u2 = yw+pw+bw
u3 = oh+yh
u4 = bh
u5 = oh+gh+ph
u6 = yw+gw+bw
P = [ow*oh,yw*yh,pw*ph,bw*bh,gw*gh]
U=[u1,u2,u3,u4,u5,u6]
l=len(U)
E=[]
E.append(Eq(oh,3))
for i in range(l):
    for j in range(i):
        e = U[i]-U[j]
        E.append(Eq(e,0))
l=len(P)
for i in range(l):
    for j in range(i):
        e = P[i]-P[j]
        E.append(Eq(e,0))
S = solve(E)
print(S)
L = 3 + S[0][yh]
print("L=",L)
