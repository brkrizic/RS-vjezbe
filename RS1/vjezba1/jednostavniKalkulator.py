# Unos podataka
broj1 = float(input("Unesite prvi broj: "))
broj2 = float(input("Unesite drugi broj: "))
operator = input("Unesite operator (+, -, *, /): ")

# Obrada i ispis rezultata
if operator == '+':
    rezultat = broj1 + broj2
    print(f"Rezultat operacije: {broj1} + {broj2} = {rezultat}")
elif operator == '-':
    rezultat = broj1 - broj2
    print(f"Rezultat operacije: {broj1} - {broj2} = {rezultat}")
elif operator == '*':
    rezultat = broj1 * broj2
    print(f"Rezultat: {broj1} * {broj2} = {rezultat}")
elif operator == '/':
    if broj2 == 0:
        print("Dijeljenje s nulom nije dozvoljeno!")
    else:
        rezultat = broj1 / broj2
        print(f"Rezultat operacije: {broj1} / {broj2} = {rezultat}")
else:
    print("Nepodržani operator!")