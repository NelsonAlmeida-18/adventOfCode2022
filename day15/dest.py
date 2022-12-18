def imprimeTabuleiro(tabuleiro):
    pos = 0
    for i in tabuleiro:
        if pos < 10:
            print(f"0{pos}: {''.join(i)}")
        else:
            print(f"{pos}: {''.join(i)}")
        pos += 1


tabuleiro = [["." for k in range(10)] for j in range(10)]

centrox, centroy = 5, 5
tamanho = 3
escreve = 1


def draw_rays(n, tabuleiro):
    escreve = 1
    espacos = 9
    for y1 in range(espacos):
        for x1 in range(escreve):
            tabuleiro[y1][espacos+x1] = "#"
        espacos -= 1
        escreve += 2

    imprimeTabuleiro(tabuleiro)


# call the function to draw the tree
draw_rays(4, tabuleiro)
