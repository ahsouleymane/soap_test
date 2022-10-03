from zeep import Client

client = Client(wsdl='http://www.dneonline.com/calculator.asmx?wsdl')
result_add = client.service.Add(10, 12)
print(result_add)