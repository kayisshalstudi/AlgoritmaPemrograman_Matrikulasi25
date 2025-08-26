# input
n = int(input())

# pengecekkan nilai n
if n > 25:

  # pengisian array sejumlah n
  number = [0] * n

  # input data
  print("")
  for i in range(n):
    number[i] = int(input())

  print("n = ", n)

  # sorting data dari kecil ke besar
  for i in range(n):
    for j in range(0, n-i-1):
      if number[j] > number[j+1]:
        temp = number[j]
        number[j] = number[j+1]
        number[j+1] = temp   

  # menghitung mean
  total = 0 
  for i in range(n):
    total = total + number[i]
    rata_rata = total / n
  print("\nMean = ", rata_rata)

  # menghitung max dan min
  maximum = number[n-1]
  minimum = number[0]

  print("Max = ", maximum)
  print("Min = ", minimum)

  # menghitung median untuk data dengan n ganjil
  if n % 2 == 1:
    indeks_tengah = int((n + 1) / 2)
    median = number[indeks_tengah-1]
    print("Median = ", median)
  
  # menghitung median untuk data dengan n genap
  else:
    indeks_tengah = int(n / 2)
    median = (number[indeks_tengah] + number[indeks_tengah-1]) / 2
    print("Median = ", median)

  # 10 bilangan terbesar
  print("\n10 bilangan terbesar: ")
  for i in range(n-1, n-11, -1):
    print(number[i])
