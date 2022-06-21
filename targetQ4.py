SP = float(67836.43)
RJ = float(36678.66)
MG = float(29229.88)
ES = float(27165.48)
outros = float(19849.53)

valor_total = (SP + RJ + MG + ES + outros)
sao_paulo = (100 * SP) / valor_total
rio_de_janeiro = (100 * RJ) / valor_total
minas_gerais = (100 * MG) / valor_total
espirito_santo = (100 * ES) / valor_total
demais_estados = (100 * outros) / valor_total

print("Representação percentual de São Paulo: " + str(sao_paulo) + "%")
print("Representação percentual do Rio de Janeiro: " + str(rio_de_janeiro) + "%")
print("Representação percentual de Minas Geraiso: " + str(minas_gerais) + "%")
print("Representação percentual de Espirito Santo: " + str(espirito_santo) + "%")
print("Representação percentual dos demais estados: " + str(demais_estados) + "%")
