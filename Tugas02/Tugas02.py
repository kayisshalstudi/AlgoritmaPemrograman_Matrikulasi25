A = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

B = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

AB = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(3):
    for j in range(3):
        A[i][j] = int(input())

print("\n")

for i in range(3):
    for j in range(3):
        B[i][j] = int(input())

def penambahan_matriks(matrix1, matrix2):
    for i in range(3):
        for j in range(3):
            AB[i][j] = matrix1[i][j] + matrix2[i][j]
    print(AB)

def pengurangan_matriks(matrix1, matrix2):
    for i in range(3):
        for j in range(3):
            AB[i][j] = matrix1[i][j] - matrix2[i][j]
    print(AB)

def perkalian_matriks(matrix1, matrix2):
    for i in range(3):
        for j in range(3):
            for k in range(3):
                AB[i][j] = AB[i][j] + matrix1[i][k] + matrix2[k][j]
    print(AB)

def cek_matriks_satuan(matriks, name):
    isSatuan = True
    for i in range(3):
        for j in range(3):
            if matriks[i][j] != 0 and matriks[i][j] != 1:
                isSatuan = False
    if isSatuan :
        print("Matriks ", name, " adalah matriks satuan")
    else:
        print("Matriks ", name, " bukan matriks satuan")

print("\n")
menu = input()
if menu == '1' :
    penambahan_matriks(A, B)
elif menu == '2':
    pengurangan_matriks(A, B)
elif menu == '3':
    perkalian_matriks(A, B)
elif menu == '4':
    cek_matriks_satuan(A, 'A')
    cek_matriks_satuan(B, 'B')
else:
    print("Bukan pilihan yang benar")