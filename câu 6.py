def minmax(S):
   min(S)
   max(S)
   print("Phần tử lớn nhất: ", max(S))
   print("Phần tử nhỏ nhất: ", min(S))

   indexMax = S.index(max(S))
   indexMin = S.index(min(S))
   print("Vị trí phần tử lớn nhất: ", indexMax)
   print("Vị trí phần tử nhỏ nhất: ", indexMin)

S = input("List cần kiểm tra: ").split()
minmax(S)