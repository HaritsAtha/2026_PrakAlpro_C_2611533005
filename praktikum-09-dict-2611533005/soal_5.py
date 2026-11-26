n = int(input())

cash = {}

for i in range(n):
    data = input().split()
    nama = data[0]
    nominal = int(data[1])

    if nama in cash:
        cash[nama] += nominal
    else:
        cash[nama] = nominal

total = sum(cash.values())

top = max(cash, key=cash.get)

for nama, jumlah in cash.items():
    print(f"{nama}: {jumlah}")

print(f"Total cash: {total}")
print(f"Top contributor: {top} ({cash[top]})")