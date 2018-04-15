# coding=utf-8
import util.io as io
import colorama

colorama.init()

input("A")
table = io.Table(["Erste", "Zweite", "Dritte", "Hase", "Schule"])
table.ZeileHinzufügen(["01", "02", "03"])
table.ZeileHinzufügen(["11", "12", "13"])
#table.RandStielHorizontal = {0:"S", 1:"D", 2:"N"}
table.GibTabelleAus(4, flush=True, RandPrefix=colorama.Fore.CYAN, InhaltPrefix=colorama.Fore.RED)
input("E")