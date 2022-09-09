import time
start = time.time()
test = [1, 1]
print("Hello World")
for i in test:
    a = input("Add number?")
    try:
        test.append(int(a))
    except ValueError:
        break
print(test)
end = time.time()
print(end-start)