

def is_rotation(s1,s2):
    tmp = s1 + s1
    return s2 in tmp


def main():
    s1 = 'waterbottle'
    s2 = 'erbottlewat'
    print(is_rotation(s1,s2))

if __name__ == "__main__":
    main()
