from BRIAN import BRIAN
def core(r="", a=""):
    print r;
    z = raw_input("YOU: ");
    r = BRIAN(z,a)
    core(z,r);
core();
