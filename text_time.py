try:
    with open ("order.txt", "r") as file:
        for line in file.readlines():
            if line != '\n':
                print(line.rstrip("\n").replace("Cheese", "Deliciousness"))
except FileNotFoundError as errmsg: # as assigns error message.
    print("That file doesn't exist, yet!")
    print(errmsg)
finally:
    print("\n---Execution Complete---")


def write_to_file(file, order_item):
    try:
        with open(file, "x") as file:
            file.write(order_item + "\n")
    except FileNotFoundError as errmsg:
        print("File cannot be found")
        print(errmsg)

write_to_file("order.txt", "Sandwich")
write_to_file("order.txt", "Dragon")
write_to_file("order.txt", "Milk")
write_to_file("order.txt", "Sebastian")
write_to_file("order.txt", "Dragonball Z")
write_to_file("order.txt", "Sandman")
write_to_file("order.txt", "Nade")