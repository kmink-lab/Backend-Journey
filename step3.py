import itertools

s,k = input().split()
k = int(k)

#for p in itertools.permutations(s,k):
#    print("".join(sorted(set(p))))

#for p in set(itertools.permutations(s, k)):
#    print("".join(p))

unique_perms = sorted(set(''.join(p) for p in itertools.permutations(s, k)))

for perm in unique_perms:
    print(perm)