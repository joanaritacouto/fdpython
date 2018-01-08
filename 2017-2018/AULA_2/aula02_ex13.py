#encoding:utf8

PF=20
PC=24.95
SPA=0.20
IMP=0.23

Lucro=((PC-SPA)/1.23-PF)*500
IMP_total=PC*0.23*500
taxas=0.20*500

print("A livraria possui um lucro de {:.2f} euros.".format(Lucro))
print("Foram coletados {} euros em importos.".format(IMP_total))
print("Foram reunidos {} euros em taxas.".format(taxas))
