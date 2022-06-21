"""
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.
"""

def make_readable(number):
    if type(number) is int and number > 0 and number < 360000:
        const = 60
        seconds_extra = 0
        if (number // const) >= 59:
            num1 = number // const
            seconds = number - (num1 * const)
            if seconds >= 10:
                seconds_extra = ''

            if (num1 // const) <= 99:
                hours = num1 // const
                mins = num1 - (hours * const)
                hours_extra, mins_extra = 0, 0
                if hours > 9:
                    hours_extra = ''
                if mins > 9:
                    mins_extra = ''

                return f"{hours_extra}{hours}:{mins_extra}{mins}:{seconds_extra}{seconds}"

        else:
            mins = number // const
            seconds = number - (mins * const)
            seconds_extra, mins_extra = 0, 0
            if mins > 9:
                mins_extra = ''
            if seconds > 10:
                seconds_extra = ''

            return f"00:{mins_extra}{mins}:{seconds_extra}{seconds}"
    else:
        return "00:00:00"