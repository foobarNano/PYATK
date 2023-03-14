 answers = []

q1dict = {
    "q": "Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie:",
    "a": "oglądanie telewizji/filmów/seriali",
    "b": "czytanie książek/czasopism",
    "c": "słuchanie muzyki"
}
print(q1dict["q"])
print("\ta) " + q1dict["a"])
print("\tb) " + q1dict["b"])
print("\tc) " + q1dict["c"])
answers.append(input("Odpowiedz: ")[0])

q2dict = {
    "q": "W jakich okolicznościach czytasz książki najczęściej?",
    "a": "podczas podróży",
    "b": "w czasie wolnym (po pracy, na urlopie)",
    "c": "podczas pracy/nauki (to ich element)"
}
print(q2dict["q"])
print("\ta) " + q1dict["a"])
print("\tb) " + q1dict["b"])
print("\tc) " + q1dict["c"])
answers.append(input("Odpowiedz: ")[0])

q3dict = {
    "q": "Jeżeli spędzasz czas wolny czytając książki, jaki jest główny powód takiego wyboru?",
    "a": "chęć poszerzenia wiedzy",
    "b": "czytanie mnie relaksuje/odpręża",
    "c": "konieczność nauki w związku z wykonywaną pracą/studiami"
}
print(q3dict["q"])
print("\ta) " + q1dict["a"])
print("\tb) " + q1dict["b"])
print("\tc) " + q1dict["c"])
answers.append(input("Odpowiedz: ")[0])

q4dict = {
    "q": "Po książki w jakiej formie sięgasz najczęściej?",
    "a": "papierowej (tradycyjnej)",
    "b": "e-booki (książki elektroniczne) na komputerze",
    "c": "e-booki na specjalnym czytniku (np. Kindle)"
}
print(q4dict["q"])
print("\ta) " + q1dict["a"])
print("\tb) " + q1dict["b"])
print("\tc) " + q1dict["c"])
answers.append(input("Odpowiedz: ")[0])

q5dict = {
    "q": "Ile książek czytasz średnio w ciągu roku?",
    "a": "żadnej w całości - jedynie fragmenty",
    "b": "1 do 3",
    "c": "4 lub więcej"
}
print(q5dict["q"])
print("\ta) " + q1dict["a"])
print("\tb) " + q1dict["b"])
print("\tc) " + q1dict["c"])
answers.append(input("Odpowiedz: ")[0])

q6dict = {
    "q": "Jak często średnio czytasz książki?",
    "a": "kilka razy w tygodniu",
    "b": "kilka razy w miesiącu",
    "c": "rzadziej"
}
print(q6dict["q"])
print("\ta) " + q1dict["a"])
print("\tb) " + q1dict["b"])
print("\tc) " + q1dict["c"])
answers.append(input("Odpowiedz: ")[0])

q7dict = {
    "q": "Po jakie gatunki książek sięgasz najczęściej?",
    "a": "horrory/thrillery",
    "b": "naukowe",
    "c": "fantastyka"
}
print(q7dict["q"])
print("\ta) " + q1dict["a"])
print("\tb) " + q1dict["b"])
print("\tc) " + q1dict["c"])
answers.append(input("Odpowiedz: ")[0])

print("pytanie: " + q1dict["q"])
print("odpowiedź: " + q1dict[answers[0]])

print("pytanie: " + q2dict["q"])
print("odpowiedź: " + q2dict[answers[1]])

print("pytanie: " + q3dict["q"])
print("odpowiedź: " + q3dict[answers[2]])

print("pytanie: " + q4dict["q"])
print("odpowiedź: " + q4dict[answers[3]])

print("pytanie: " + q5dict["q"])
print("odpowiedź: " + q5dict[answers[4]])

print("pytanie: " + q6dict["q"])
print("odpowiedź: " + q6dict[answers[5]])

print("pytanie: " + q7dict["q"])
print("odpowiedź: " + q7dict[answers[6]])
