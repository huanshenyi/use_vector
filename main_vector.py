from useVector.Vector import Vector

if __name__ == "__main__":

    vec = Vector([5, 2])
    print(vec) # (5, 2)
    print(len(vec)) # 2
    print(vec[0]) # 5

    vec2 = Vector([3, 1])
    print(vec + vec2)  # (8, 6)
    print(vec - vec2)  # (2, 1)
    print(vec * 2)     # (10, 4)
    print(2 * vec)     # (10, 4)

    print(-vec)        # (-5, -2)
    print(+vec)        # (5, 2)

    zero2 = Vector.zero(2)
    print(zero2)

    print(vec.norm())  # 5.385164807134504

    print(vec.normalize().norm()) # 1.0

    try:
        zero2.normalize()
    except ZeroDivisionError:
        print("Cannot normalize zero vector{}".format(zero2))
