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
  return tbl					#lista de tuplos com (nome , data,...)

def printTable(tbl):
  for reg in tbl:
    name, data, pabertura, pmax, pmin, pfecho, vol = reg
    print("{:8s} {:12s} {:12.2f} {:12.2f} {:12.2f} {:12.2f} {:10d}".format(name, data, pabertura, pmax, pmin, pfecho, vol))
		lambda t: t[6]

          
def main():
  tbl = loadfile('stocks.csv') #tbl variável
  tbl2 = sorted(tbl, key=lambda t:(t[1], t[0]) )
  printTable (tbl2)

main()
