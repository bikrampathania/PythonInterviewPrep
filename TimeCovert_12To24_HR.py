'''
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock.
Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.

Input: 07:05:45PM
Output: 19:05:45
'''

def timeConversion(s):

    hrs12 = s[:2]
    hrs24 = int(hrs12) + 12
    mins = s[3:5]
    secs = s[6:8]
    ampm = s[8:10]

    if int(hrs12) == 12 and ampm == 'AM':
        return ('00' + ':' + (mins) + ':' + (secs))

    if int(hrs12) == 12 and ampm == 'PM':
        return ('12' + ':' + (mins) + ':' + (secs))
    
    if int(hrs12[0]) == 0 and 1 <= int(hrs12) < 10 and ampm == 'AM':
        return ((hrs12) + ':' + (mins) + ':' + (secs))
    elif 10 <= int(hrs12) < 12 and ampm == 'AM':
        return ((hrs12) + ':' + (mins) + ':' + (secs))
    elif int(hrs12[0]) == 0 and 1 <= int(hrs12) < 10 and ampm == 'PM':
        return (str(hrs24) + ':' + (mins) + ':' + (secs))
    elif 10 <= int(hrs12) < 12 and ampm == 'PM':
        return (str(hrs24) + ':' + (mins) + ':' + (secs))
    else:
        return None

'''
print(timeConversion('02:05:45AM'))

02:05:45
'''

