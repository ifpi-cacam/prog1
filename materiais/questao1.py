tupla = (15, 'Marcelo Alves', 7.73, [])

print('Primeiro elemento da tupla: ', tupla[0])
print('Terceiro elemento da tupla: ', tupla[2])

# Primeira forma
tupla_ = (100, 'Python', 7.73, [])

tupla_ = (100, 'Python', tupla[2], tupla[3])



print(tupla_)