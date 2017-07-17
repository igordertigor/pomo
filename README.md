# pomo basic pomodoro timer

I was a little annoyed by the pomodori timers out there. Most of them count
down to zero beep once and that's it. Yet, if you're focussing on something,
you might actually miss the beep sound and because you're so focussed, you may
catch yourself spending 2 hours on something that you wanted to actually just
spend 25 minutes on. Yet, it seems as if there are virtually no pomodori times
out there that have a "snooze" functionality. After looking for half an hour, I
decided that I should be able to write one in half an hour. Well, the first
draft took about that long. With a little brushing, it was more like an hour
and a half. So here is what you get with `pomo`:

- *Countdown*: While your work (or break) interval is running, you get a simple
  countdown that shows how much time is left (minutes:seconds). If you are over
  time, it clearly shows that you are, but keeps counting the time.
- *Reminder sound*: When the interval is over, a reminder sound is played. Yet,
  the timer keeps running until you explicitly indicate that you're done. The
  sound is played again after a snooze time of three minutes.
- *Logging*: If you like, you can specify a log file to write the full duration
  of each interval to.
- *Done at any time*: When you're done, you're done. Most naive implementations
  of pomodori timers run until the interval is over. You can't simply stop half
  way through. With `pomo`, you just press "d" to indicate that you're done.
- *Action hooks*: Add your own actions to perform during a running interval.
  These can be triggered by any key combination typed during the interval.
- *Terminal*: Clearly, this is a terminal application.


## Installation

Pomo is on pypi, so a simple
```
pip install pomo
```
should do.

If you want to install pomo from source, you need [pybuilder](http://pybuilder.github.io/) and the [source](https://github.com/igordertigor/pomo). Then, a simple
```
pyb install
```
will do the installation for you


## Basic usage

Basic usage information can be obtained by typing
```
pomo -h
```
There are currently three hard coded durations: `work` (25 min), `short` (5 min), and `long` (15 min). So you can use
```
pomo work write readme for pomo
```
to start working on the tast "write readme for pomo". You don't have to give a
task description, but it is often useful when you want to do a review of your
tasks at the end of the day.
