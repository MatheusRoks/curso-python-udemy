#temos alguns detalhes que precisam ser tratados. 
#dir= exibe quais metodos uma determinada função pode receber.
# hasattr = verifica se uma determinada variável possui o método desejado
# getattr = executa o metodo que ele pegou, vamos aos exemplos.
string = 'Matheus'
metod = "upper"

if hasattr(string, metod):
    print('existe upper pra str')
    print(getattr(string, metod)())
else:
    print('sla mané')