print("overall grade")
def get_float(number):
    while True:
        try:
            float_number = float(input(f"enter mark {number} : "))
            return float_number
        except ValueError:
            print("please enter a valid mark")
        continue
first_mark = get_float(1)
first_weight = int(input("enter first weight >"))
print()
second_mark = get_float(2)
second_weight = int(input("enter second weight >"))
print()
third_mark = get_float(3)
third_weight = int(input("enter third weight >"))
print()
print("overall mark for weight>")
print("first mark is >", first_mark)
print("first weight is >", first_weight)
print("second mark is >", second_mark)
print("second weight is >", second_weight)
print("third mark is >", third_mark)
print("third weight is >", third_weight)
overalmark1 = first_mark*first_weight
print("total first mark is>")
print(f"{overalmark1: .3f}%")
overalmark2 = second_mark*second_weight
print("total second mark is>")
print(f"{overalmark2:.3f}%")
overalmark3 = third_mark*third_weight
print("total second mark is>")
print(f"{overalmark3: .3f}%")
overal = (overalmark1 + overalmark2 + overalmark3)
print("overal mark percent>")
print(f"{overal:.3f}%")