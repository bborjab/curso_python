to_do = ["Dirigirnos al hotel", "Ir a almorzar", "Visitar un museo", "Regresar a un hotel"]

print(to_do)

mix = ["Uno", 2, True, [1, 2, 3]]

print(mix)
print(mix[0:2])
mix.append(False)
print(mix)
mix.insert(2, ["Caro"])
print(mix)
print(mix.index(2))
del mix[2]
print(mix)