url = "https://bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real"

print(url)

indice_interrogacao = url.find('?')

url_base = url[:indice_interrogacao]
url_parametros = url[indice_interrogacao+1:]
parametro_busca = 'moedaDestino'
indice_parametro = url_parametros.find(parametro_busca)

indice_valor = indice_parametro + len(parametro_busca) + 1
valor = url_parametros[indice_valor:]


print(url_base)
print(url_parametros)
print(indice_parametro)
print(valor)


