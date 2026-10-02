import statistics as st

x = [10,20,30,40]

print (st.mean(x))

z = {10,20,30,40}

print (st.mean(z))

s = (10,20,30,40)

print (st.mean(s))

a = st.harmonic_mean ([1,2])

print (a)

b = st.harmonic_mean ([7,2,3,6,9,33,2.5])

print (b)

c = st.median ([3,6,9,4,5,3.2,9,7])

print(c)

e = st.median ([3,6,9,4,20,3.2,9,7])

print(e)

t = st.median_low ([3,6,9,4,5,3.2,9,7,9])

print (t)

w = st.median_high ([3,6,9,4,5,3.2,9,7,9])

print (w)

v = st.mode([2, 3, 5, 4, 2, 3, 6, 9, 5, 8, 2, 2, 3, 4, 6])

print(v)

p = st.stdev ([3.2,6.9,8.1,-9.3,66])

print(p)

u = st.variance ([3.2,6.9,8.1,-9.3,66])

print(u)