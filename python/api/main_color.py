# coding: utf-8
# !/usr/bin/python

class color:

    def __init__(self):  # Notre méthode constructeur
        pass

    # TEST
    # ============================================================

    def TEST(self):
        return "\033[1m"

    # NEUTRE
    # ============================================================

    def NEUTRE(self):
        return "\033[0m"

    def DEFAULT(self):
        return "\033[0m"

    # STYLE
    # ============================================================

    def GRAS(self):
        return "\033[1m"

    def SOULIGNE(self):
        return "\033[4m"

    def ITALIQUE(self):
        return "\033[3m"

    def BLINK(self):
        return "\033[5m"

    def REVERSE(self):
        return "\033[7m"

    def CANCELED(self):
        return "\033[8m"

    def BARRE(self):
        return "\033[9m"

    # COULEUR
    # ============================================================

    def GRIS2(self):
        return "\033[30m"

    def ROUGE2(self):
        return "\033[31m"

    def VERT2(self):
        return "\033[32m"

    def JAUNE2(self):
        return "\033[33m"

    def BLEU2(self):
        return "\033[34m"

    def MAGENTA2(self):
        return "\033[35m"

    def CYAN2(self):
        return "\033[36m"

    def BLANC2(self):
        return "\033[37m"

    # COULEUR 2
    # ============================================================

    def GRIS(self):
        return "\033[90m"

    def ROUGE(self):
        return "\033[91m"

    def VERT(self):
        return "\033[92m"

    def JAUNE(self):
        return "\033[93m"

    def BLEU(self):
        return "\033[94m"

    def MAGENTA(self):
        return "\033[95m"

    def CYAN(self):
        return "\033[96m"

    def BLANC(self):
        return "\033[97m"

    # BACKGROUND
    # ============================================================

    def GRIS2_BCK(self):
        return "\033[40m"

    def ROUGE2_BCK(self):
        return "\033[41m"

    def VERT2_BCK(self):
        return "\033[42m"

    def JAUNE2_BCK(self):
        return "\033[43m"

    def BLEU2_BCK(self):
        return "\033[44m"

    def MAGENTA2_BCK(self):
        return "\033[45m"

    def CYAN2_BCK(self):
        return "\033[46m"

    def BLANC2_BCK(self):
        return "\033[47m"

    # BACKGROUND 2
    # ============================================================

    def GRIS_BCK(self):
        return "\033[100m"

    def ROUGE_BCK(self):
        return "\033[101m"

    def VERT_BCK(self):
        return "\033[102m"

    def JAUNE_BCK(self):
        return "\033[103m"

    def BLEU_BCK(self):
        return "\033[104m"

    def MAGENTA_BCK(self):
        return "\033[105m"

    def CYAN_BCK(self):
        return "\033[106m"

    def BLANC_BCK(self):
        return "\033[107m"
