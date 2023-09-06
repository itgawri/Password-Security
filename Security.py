password_length = 6
counter = 1
permutations = 1

while counter <= password_length:
  permutations = permutations * counter
  counter += 1

print(f"The possible combination of a {password_length}-character password is: {permutations}")

attempts = 5
max_lock = permutations / attempts
max_lock = int(max_lock)
print(f"The maximum number of times the account might be locked is {max_lock} times.")

locks = 0
total_lock_time = 0
lock_time_multiplier = 5

for i in range(max_lock):
  locks += 1
  total_lock_time += locks * lock_time_multiplier
  print(f"Your account is locked for {lock_time_multiplier*locks} minutes")

print(f"Assuming the hacker only got the password right with the last possible combination, your account would have been locked for {total_lock_time} minutes in total.")

# PL------------------------------------------------------------------------------------------

dlugosc_hasla = 6
licznik = 1
permutacje = 1

while licznik <= dlugosc_hasla:
  permutacje = permutacje * licznik
  licznik += 1

print(f"Liczba możliwych kombinacji hasła o długości {dlugosc_hasla} znaków wynosi: {permutacje}")

proby = 5
maksymalna_liczba_blokad = permutacje / proby
maksymalna_liczba_blokad = int(maksymalna_liczba_blokad)
print(f"Maksymalna liczba blokad konta to {maksymalna_liczba_blokad} razy.")

blokady = 0
calkowity_czas_blokady = 0
mnoznik_czasu_blokady = 5

for i in range(maksymalna_liczba_blokad):
  blokady += 1
  calkowity_czas_blokady += blokady * mnoznik_czasu_blokady
  print(f"Twoje konto jest zablokowane na {mnoznik_czasu_blokady*blokady} minut")

print(f"Zakładając, że haker odgadł hasło dopiero przy ostatniej możliwej kombinacji, Twoje konto byłoby zablokowane przez {calkowity_czas_blokady} minut w sumie.")
