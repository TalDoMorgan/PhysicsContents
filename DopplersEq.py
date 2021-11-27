print("Legenda:")
print("V = velocidade da onda no meio;")
print("Vo = velocidade do objeto em relacao à fonte;")
print("Vs = velocidade da fonte em relacao ao meio;")
print("FreqS = frequencia da fonte\n")
print("Equacao: FreqS * ((V+Vo) / (V-Vs))")
      
V = input("Insira aqui a velocidade da onda (m/s): \n")
Vo = input("Insira aqui a velocidade do observador (m/s): \n")
Vs = input("Insira aqui a velocidade da fonte (m/s): \n")
FreqS = input("Insira aqui a frequencia da fonte (Hz): \n")

Eq = float(FreqS) * ((float(V)+float(Vo)) / (float(V)-float(Vs)))

print("Frequencia observada =",Eq,"Hz")