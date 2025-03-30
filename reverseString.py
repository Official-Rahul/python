def reverse(str):
    i, j = 0, len(str)-1
    result = ""
    while j>=i:
        result+=str[j]
        j-=1
    return result

print(reverse("rahul"))
print(reverse("ashu"))