import util.io as io
import colorama

table = io.Table(["Erste", "Zweite", "Dritte"])
table.ZeileHinzufügen(["01", "02", "03"])
table.ZeileHinzufügen(["11", "12", "13"])
print(table.BerechneZellenLaenge(4))
print(table.Zellen)
input("A")