def time_string(hours, minutes, time_format):
    if time_format == '24':
        return f"{hours:02}:{minutes:02}"
    elif time_format == '12':
        suffix = 'am'
        h = hours
        if hours >= 12:
            suffix = 'pm'
            if hours > 12:
                h -= 12
        if h == 0:
            h = 12
        return f"{h}:{minutes:02}{suffix}"
    return "Invalid format"

print(f"time_string(15, 38, '24') returns '{time_string(15, 38, '24')}'")
print(f"time_string(8, 3, '24') returns '{time_string(8, 3, '24')}'")
print(f"time_string(0, 5, '24') returns '{time_string(0, 5, '24')}'")
print(f"time_string(11, 15, '12') returns '{time_string(11, 15, '12')}'")
print(f"time_string(0, 7, '12') returns '{time_string(0, 7, '12')}'")
print(f"time_string(7, 30, '12') returns '{time_string(7, 30, '12')}'")
print(f"time_string(12, 46, '12') returns '{time_string(12, 46, '12')}'")
print(f"time_string(13, 10, '12') returns '{time_string(13, 10, '12')}'")
print(f"time_string(19, 02, '12') returns '{time_string(19, 2, '12')}'")
