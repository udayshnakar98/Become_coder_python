def movezeros(n,data):
    for i in data:
        if i==0:
            data.remove(i)
            data.append(i)

n=int(input())
data=list(map(int,input().split()))
movezeros(n,data)
print(*data)
