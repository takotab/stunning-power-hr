class Person(object):
    def __init__(self, ftp=None, aneroob=None):
        self.ftp, self.aneroob = ftp, aneroob
        self.current_aneroob = aneroob

    def cycle(self, power, time):
        for t in range(time):
            if power > self.ftp:
                self.current_aneroob = self.current_aneroob - (power - self.ftp)
                if self.current_aneroob < 0:
                    print("Was only able to do " + str(t) + "(sec) on " + str(power))
                    return False
        print("Done cycling at " + str(power) + " W/t " + str(time) + "(sec)")
        print(self)
        print("---")
        return True

    def __str__(self):
        s = "ftp: " + str(self.ftp) + "(W) aneroob: " + str(self.aneroob) + "(kJ)"
        s += "current aneroob:" + str(self.current_aneroob)
        return s
