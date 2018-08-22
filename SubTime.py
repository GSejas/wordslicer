class Time(object):
    seconds = 0.0
    minutes = 0
    hours = 0

    def __init__(self, h, m, s):
        self.seconds = s
        self.minutes = m
        self.hours = h

    def __add__(self, other):
        extraMin = 0
        extraHr = 0
        newsec = self.seconds + other.seconds
        if newsec > 60:
            newsec = newsec % 60
            extraMin = 1
        newmin = self.minutes + other.minutes + extraMin
        if newmin > 60:
            newmin = newmin % 60
            extraHr = 1
        newhr = self.hours + other.hours + extraHr
        return Time(newhr, newmin, newsec)

    def __sub__(self, other):
        subMin = 0
        subHr = 0
        newsec = self.seconds - other.seconds
        if newsec < 0:
            newsec = newsec % 60
            subMin = 1
        newmin = self.minutes - other.minutes - subMin
        if newmin < 0:
            newmin = newmin % 60
            subHr = 1
        newhr = self.hours - other.hours - subHr
        return Time(newhr, newmin, newsec)
    def Print(self):
        return "%02d:%02d:%06.3f" % (self.hours, self.minutes, self.seconds)