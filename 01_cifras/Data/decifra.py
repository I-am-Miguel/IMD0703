import sys

if __name__ == "__main__":

    data = sys.argv[1]
    cif = sys.argv[2]
    text = sys.argv[3]

    c = open(cif, "r")
    t = open(text, "w+")

    for palavra in c:
        print (palavra)
    c.close()