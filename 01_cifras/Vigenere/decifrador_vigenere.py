
def decifra_vigenere(mensagem_cifrada, key):
    mensagem_cifrada_original = mensagem_cifrada

    #mensagem_cifrada = removerAcentosECaracteresEspeciais(mensagem_cifrada, "áéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ:")

    key = key * len(mensagem_cifrada)
    mensagem_decifrada = ""
    mensagem_cifrada_copia = "".join(mensagem_cifrada.split())
    indice_espaco = 0

    for letra_cifrada, letra_key in zip(mensagem_cifrada_copia, key):

        letra_cifrada_original_ascii = ord(mensagem_cifrada_original[indice_espaco].upper()) - 65
        if letra_cifrada_original_ascii < 0 or letra_cifrada_original_ascii > 25:
            mensagem_decifrada += mensagem_cifrada_original[indice_espaco]
            indice_espaco += 1

        mensagem_decifrada += mapeamento_vinegere(letra_cifrada, letra_key)
        indice_espaco += 1

    return mensagem_decifrada


def mapeamento_vinegere(letra_cifrada, letra_key):
    return deslocar_letra(letra_cifrada, letra_key)


def deslocar_letra(letra_encriptada, letra_key):
    letra_encriptada_ascii = ord(letra_encriptada.upper()) - 65
    letra_key_ascii = ord(letra_key.upper()) - 65

    if letra_encriptada_ascii < 0 or letra_encriptada_ascii > 25:
        return letra_encriptada

    referencia_letra_encriptada_numerica = (letra_encriptada_ascii) % 26
    referencia_letra_key_numerica = (letra_key_ascii) % 26
    nova_letra = chr(((referencia_letra_encriptada_numerica - referencia_letra_key_numerica) % 26) + 65)

    return nova_letra


def removerAcentosECaracteresEspeciais(old, to_remove):
    new_string = old
    for x in to_remove:
        new_string = new_string.replace(x, '')
    return new_string


if __name__ == '__main__':
    KEY = 'DESPACITO'

    arquivo_cifrado = open('./arquivos/musica_teste.txt', 'r')
    arquivo_decifrado = open('./arquivos/musica_decifrada.txt', 'w')

    mensagem_sem_acento = arquivo_cifrado.read()

    texto_decifrado = decifra_vigenere(mensagem_sem_acento, KEY)

    arquivo_decifrado.write(texto_decifrado)

    arquivo_cifrado.close()
    arquivo_decifrado.close()
