lenci: str = "Vinícius Lenci"

print(f"Lenci = '{lenci}'")  # Forma tradicional

print(f"{lenci = }")  # Forma nova com fstring

# Debug vem aqui, porque dá pra ver o que foi feito para ter aquele resultado
print(f"{lenci.upper()[::-1] = }")
