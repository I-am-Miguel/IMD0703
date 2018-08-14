import sys

if __name__ == "__main__":

    data = sys.argv[1]
    text = sys.argv[2]
    cif = sys.argv[3]

    t = open(text, "r")
    c = open(cif, "w+")

    for palavra in t:
        print (palavra)
    t.close()