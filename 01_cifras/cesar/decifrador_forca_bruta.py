def deslocar_letra(letra, posicao):
    valor_ascii = ord(letra.upper()) - 65

    if valor_ascii < 0 or valor_ascii > 25:
        return letra

    referencia_numerica = (valor_ascii) % 26
    nova_letra = chr(((referencia_numerica + posicao) % 26) + 65)

    return nova_letra


if __name__ == '__main__':

    arquivo_cifrado = open('./arquivos/mensagem_cifrada.txt', 'r')
    arquivo_decifrado = open('./arquivos/mensagem_decifrada.txt', 'w')

    texto_cifrado = arquivo_cifrado.read()
    texto_decifrado = ''
    msg_deslocamento = ''
    for deslocamento in range(26):

        msg_deslocamento = "Utilizando o deslocamento em[{}]\n".format(deslocamento)
        for letra_cifrada in texto_cifrado:
            texto_decifrado += deslocar_letra(letra_cifrada, -deslocamento)

        print(msg_deslocamento)
        print(texto_decifrado)
        print("Deseja finalizar(s/n)?")
        finalizar = input()
        if finalizar.upper() == 's'.upper():
            break

        texto_decifrado = ''

    arquivo_decifrado.write(msg_deslocamento + texto_decifrado)

    arquivo_cifrado.close()
    arquivo_decifrado.close()
