n = 1260
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    # // : 나누기 연산 후 소수점 이하의 수를 버린 정수부분
    count += n // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수
    n %= coin # 해당 화폐를 통해 거슬러 준 뒤 남은 돈

print(count)