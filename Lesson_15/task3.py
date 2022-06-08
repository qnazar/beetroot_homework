"""Create a simple prototype of a TV controller in Python. It’ll use the following commands:

first_channel() - turns on the first channel from the list.
last_channel() - turns on the last channel from the list.
turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
previous_channel() - turns on the previous channel. If the current channel is the first one, turns on the last channel.
current_channel() - returns the name of the current channel.
is_exist(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes", if the channel N or 'name'
exists in the list, or "No" - in the other case.

The default channel turned on before all commands is №1.

Your task is to create the TVController class and methods described above."""

CHANNELS = ["BBC", "Discovery", "TV1000"]


class TVController:
    def __init__(self, channels: list):
        self.channels: list = channels
        self.current = channels[0]

    def first_channel(self):
        self.current = self.channels[0]
        return self.current

    def last_channel(self):
        self.current = self.channels[-1]
        return self.current

    def turn_channel(self, n):
        self.current = self.channels[n-1]
        return self.current

    def next_channel(self):
        if self.current == self.channels[-1]:
            self.current = self.channels[0]
        else:
            self.current = self.channels[self.channels.index(self.current) + 1]
        return self.current

    def previous_channel(self):
        if self.current == self.channels[0]:
            self.current = self.channels[-1]
        else:
            self.current = self.channels[self.channels.index(self.current) - 1]
        return self.current

    def current_channel(self):
        return self.current

    def is_exist(self, n: int or str):
        if isinstance(n, int):
            if n > 0 and n - 1 < len(self.channels):
                return 'Yes'
        elif isinstance(n, str):
            if n in self.channels:
                return 'Yes'
        return 'No'


controller = TVController(CHANNELS)


assert controller.first_channel() == "BBC"
assert controller.last_channel() == "TV1000"
assert controller.turn_channel(1) == "BBC"
assert controller.next_channel() == "Discovery"
assert controller.previous_channel() == "BBC"
assert controller.current_channel() == "BBC"
assert controller.is_exist(4) == "No"
assert controller.is_exist("BBC") == "Yes"
