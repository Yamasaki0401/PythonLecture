# 変数へ代入：assignment
hello = "konnichwa"
world = "sekai"  # aにHello Worldを代入する  変数名を変更する場合、右クリックでrefactor,renameで同じ変数のものは一度に変更できる
print(hello + world)

# format
"hello {}".format("world") #{}に（）内の文字列を入れることができる
print("{}{}".format(hello, world))

name = "Emily"
print("Hey,{}!! How are you doing?".format(name))

balance = 100
print("balance: {}".format(balance))

# fstring　.formatより処理がはやい(python3.5以上）
print(f"{hello} {world}")

print(f"Hey,{name}!! How are you doing?")
print(f"balance: {balance}")
