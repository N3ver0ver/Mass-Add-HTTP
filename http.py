from __future__ import print_function
import os, sys, re, colorama
colorama.init(autoreset=True)

class HttpAdd():
    def __init__(self):
        self._l = []
        self._w = "\x1b[0m"
        self._r = "\x1b[91m"
        self._c = "\x1b[36m"
        self._b = "\x1b[94m"
        self._g = "\x1b[92m"
        self._y = "\x1b[33m"
        self._m = "\x1b[35m"
        if not os.path.exists("Result"):
            os.makedirs("Result")
        if os.name == "nt":
            os.system("cls")
            os.system("title "+os.getcwd()+": AddHTTP7 x N3ver0ver!")
        else:
            os.system("clear")
        if sys.version_info.major == 2:
            self.Main2()
        else:
            self.Main3()

    def print_true(self, *arg):
        print("["+self._g+"+"+self._w+"] "+arg[0]+self._g+" => "+self._w+arg[1])
        open(arg[2]+"/Http.txt","a").write(arg[1]+"\n")

    def print_false(self, *arg):
        print("["+self._r+"-"+self._w+"] "+arg[0]+self._r+" => "+self._w+arg[1])

    def print_error(self, *arg):
        if len(arg) == 2:
            print("["+self._y+"!"+self._w+"] "+arg[0]+self._y+" => "+self._w+arg[1])
        else:
            print("["+self._y+"!"+self._w+"] "+arg[0])
        sys.exit()
    
    def Add(self, url):
        try:
            if url.startswith("http://") or url.startswith("https://"):
                pass
            else:
                url = "http://"+url
            if url.split("/")[2] not in self._l:
                self._l.append(url.split("/")[2])
                self.print_true(url.split("/")[2], url, "Result")
            else:
                self.print_false(url, "Duplicate")
        except:
            pass

    def Banner(self):
        banner = """
\t    ___       __    ____  __________________  _____
\t   /   | ____/ /___/ / / / /_  __/_  __/ __ \\/__  /
\t  / /| |/ __  / __  / /_/ / / /   / / / /_/ /  / / 
\t\x1b[94m / ___ / /_/ / /_/ / __  / / /   / / / ____/  / /  \x1b[0m
\t/_/  |_\\__,_/\\__,_/_/ /_/ /_/   /_/ /_/      /_/   
\t\t\tN3ver0ver
"""
        print(banner)

    def Main2(self):
        try:
            self.Banner()
            print("["+self._b+">"+self._w+"] Enter List "+self._b+"=>"+self._w, end=""); list_site = raw_input(" ")
        except:
            self.print_error("Thank You")
        try:
            texx = open(list_site).read().splitlines()
        except:
            self.print_error("List Site Not Found")
        try:
            for t in texx:
                if t == "":
                    pass
                else:
                    self.Add(t)
        except:
            pass
    

    def Main3(self):
        try:
            self.Banner()
            print("["+self._b+">"+self._w+"] Enter List "+self._b+"=>"+self._w, end=""); list_site = input(" ")
        except:
            self.print_error("Thank You")
        try:
            texx = open(list_site).read().splitlines()
        except:
            self.print_error("List Site Not Found")
        try:
            for t in texx:
                if t == "":
                    pass
                else:
                    self.Add(t)
        except:
            pass


if __name__ == "__main__":
    try:
        HttpAdd()
    except:
        pass
