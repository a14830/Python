from random import randint
import os

nums = []

for _ in range(30):
    nums.append(randint(0, 100))

soma = sum(nums)
maior = max(nums)
menor = min(nums)
media = sum(nums) / len(nums)

acimadamedia = []
for n in nums:
    if n > media:
        acimadamedia.append(n)

print(f"Lista: {nums}")
print(f"Soma: {soma} | Maior: {maior} | Menor: {menor} | Média: {media}")
print(f"Acima da média: {acimadamedia}")





# # # Imprimir lista
# print (nums) # [2,5,8,11,7,9,13]
# # # Imprimir um elemento da lista
# print (nums[2]) # 8
# # # inserir um elemento no final
# nums.append(17) # [2,5,8,11,7,9,13,17]
# # # inserir varios elementos no final da lista
# nums.extend([12,16]) # [2,5,8,11,7,9,13 ,17,12,16]
# # # inserir em posição especifica
# nums.insert(3,29) # [2,5,8,29,7,9,13 ,17,12,16]

# # # remover um elemento no final da lista
# nums.pop() # [2,5,8,11,7,9,13,17]
# # # remover um elemento de uma posição especifica
# nums.pop(2) # [2,5,8,11,7,9,13 ,17,12,16]
# # # inserir em posição especifica
# nums.remove(17) # [2,5,8,29,7,9,13 ,17,12,16]
# # # nº de elementos da lista
# total = len(nums)

# for n in nums: # para cada elemento da minha lsita
#    if n <=10:
#         print(n,end=" ")
# for indice in range(len(nums)):
#     if nums[indice] <=10:
#         print(nums[indice], end =" ")

# nums =  [1,5,11,23,32]
# media = 22.2