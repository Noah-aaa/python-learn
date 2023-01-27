def sayhi():
    print()


print(sayhi())
print(type(sayhi()))
def check(num):
    if num >= 18:
        return "success"
    else :
        return None
result = check(16)

print(result)

if not result:
    print(f"{not result}")