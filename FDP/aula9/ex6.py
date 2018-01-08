def loadfile(fname):
  """Abre o ficheiro fname e carrega o conteúdo para uma lista de tuplos."""
  tbl = []
  file = open (fname, 'r')
  for line in file:
    t = line.split (',')
    # name, data, pabertura, pmax, pmin, pfecho, vol
    tpl = t[0], t[1], float(t[2]), float(t[3]), float(t[4]), float(t[5]), int(t[6])
    tbl.append(tpl)
  file.close()
  return tbl          #lista de tuplos com (nome , data,...)

def printTable(tbl):
  for reg in tbl:
    name, data, pabertura, pmax, pmin, pfecho, vol = reg
    print("{:8s} {:12s} {:15.f} {:15.2f} {:15.2f} {:15.2f} {:10d}".format(name, data, pabertura, pmax, pmin, pfecho, vol))
    
def main():
  tbl = loadfile('stocks.csv') #tbl variável
  printTable (tbl)
 
main() 
    

# Resolução do problema 6, semana 9.
# OUTPUT esperado:
# [('CSCO', '25-Nov-2015', 27.32, 27.389999, 27.0, 27.24, 22472500), ('CSCO', '24-Nov-2015', 27.25, 27.440001, 27.0, 27.27, 31701900), ('CSCO', '23-Nov-2015', 27.65, 27.84, 27.34, 27.43, 24684600), p(ara a frente