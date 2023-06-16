from yoclo import run

def f(a, x:int, y=1, z:str="hello"):
    print("Received values a=%s, x=%d, y=%s, z=%s" % (a, x, y, z))

if __name__ == "__main__":
    run(f)
