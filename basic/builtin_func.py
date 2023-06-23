# built in function Pythonに組み込まれている関数
# type()
hello_type = type("Hello")   # データ型を返してくれる
print(hello_type)
# print(type("Hello")) も一緒

# id() データのIDを返してくれる
hello_id = id("hello")
print(hello_id)
hello = "hello"
hello2 = "hello"
print(id(hello))
print(id(hello2))  # helloのIDは同じIDになる
