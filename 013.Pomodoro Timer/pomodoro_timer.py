import time
from notifypy import Notify

# Initiliate a Timer class to model the Pomodoro Technique
class Timer():
    def __init__(self, duration):
        self.duration = duration * 60   # Convert minutes to seconds
        self.isRunning = False
        self.beginTime = None
        self.endTime = None

    def begin(self):
        self.beginTime = time.time()
        self.isRunning = True

    def end(self):
        # End the timer and record the time
        self.endTime = time.time()
        self.isRunning = False

    def timeElapsed(self):
        # Amount of time since the timer was started
        if self.isRunning:
            return time.time() - self.beginTime
        else:
            return self.endTime - self.beginTime

    def timeRemaining(self):
        # Amount of time remaining on the timer
        return (self.duration - self.timeElapsed())

    def timeFinished(self):
        # Boolean check to see if the timer is up
        return self.timeElapsed() >= self.duration

    def resetTimer(self):
        # Reset the timer to its original condition
        self.isRunning = False
        self.duration = self.duration
        self.startTime = None
        self.endTime = None
    
def workPeriod(workDuration):
        notification = Notify()
        notification.title = "Pomodoro Timer"
        notification.message = "Time to start working again, only {} minutes left.".format(workDuration)
        notification.send()
        workTimer = Timer(workDuration)
       # Begin the timer
        workTimer.begin()
        print("Work timer has started...")
        # Wait in a loop until the 25-minute work period has elapsed
        while not workTimer.timeFinished():
            time.sleep(1)
        # End the work timer as 25 minutes are now up
        workTimer.end()
        # Reset the timer
        workTimer.resetTimer()
    
def restPeriod(restDuration):
    notification = Notify()
    notification.title = "Pomodoro Timer"
    notification.message = "Great work, you've earned a {} minute break!".format(restDuration)
    notification.send()
    # Timer objects for the work and rest periods
    restTimer = Timer(restDuration)
    # Begin the rest timer
    restTimer.begin()
    # Wait in a loop until the 5-minute rest period has elapsed
    while not restTimer.timeFinished():
        time.sleep(1)
    # End the rest timer as 5 minutes are now up
    restTimer.end()

    # Reset the timer
    restTimer.resetTimer()

def main():
    # Four work periods of 25 minutes with a 5 minute break
    # Non-user configurable time limits
    for i in range(4):
        workPeriod(25)
        restPeriod(5)
    # One more work period with a 25 minute break
    workPeriod(25)
    restPeriod(25)
    print("Full Pomodoro cycle complete.")

if __name__ == '__main__':
    main()
