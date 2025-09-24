#ustawiam klucz na 1 element w liscie i jesli klucz jest wiekszy od kazdego pojedynczego elemneyu bedacegho po prawej stronie to je przenosze na lewa strone klucza 
#hezeli natomiast po prawej stronie klucza elementy sa wieksze od niego to warunek nie zostaje spelniony i nie zamieniam elementow miejscami, zostae po prawej stronie klucza

#TOK ROZUMOWANIA

def przestaw(A):
  klucz =A[0]
  w = 0

  for k in range(1, len(A)):
    if A[k] < klucz:
    
