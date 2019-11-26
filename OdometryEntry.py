import datetime

class OdometryEntry:
    date = datetime.date(1900, 1, 1)
    odometry = 0
    cost = 0
    comment = ""

    def __init__(self, pDate, pOdometry, pCost, pComment):
        self.date = pDate
        self.odometry = pOdometry
        self.cost = pCost
        self.comment = pComment

    def printComment(self):
        print(self.comment)

    def print(self):
        print(str(self.date) + ", " + str(self.odometry) + ", " + str(self.cost) + ", " + self.comment)
