def in_autotests_we_trust(a, b):
    if a == b:
        print('Passou no teste')
    else:
        print('Falhou no teste')

in_autotests_we_trust(10, '10')

in_autotests_we_trust(0, False)

Aang = "O Aang é um airbender"
Katara = "A Katara é uma waterbender"

Avatar = f"{Aang} e {Katara}"
print(Avatar)

