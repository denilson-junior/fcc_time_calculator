def add_time(start, duration, day_of_week=""):
    new_time = 0
    start_time_converted = float(start.split()[0].replace(':', '.', 1))
    am_or_pm_time = start.split()[1]
    duration_converted = float(duration.replace(':', '.', 1))
    sum_of_time = start_time_converted + duration_converted

    if sum_of_time > 12:
        sum_of_time -= 12

        if int(str(sum_of_time)[2:4]) >= 60:
            sum_of_time += 1
            sum_of_time -= .60

        if am_or_pm_time == "AM":
            new_time = "{:.2f} PM".format(sum_of_time)
            new_time = new_time.replace('.',':',1)
        elif am_or_pm_time == "PM":
            new_time = "{:.2f} AM".format(sum_of_time)
            new_time = new_time.replace('.',':',1)
    else:
        if len(str(sum_of_time)) > 4:
            if int(str(sum_of_time)[3:5]) >= 60:
                sum_of_time += 1
                sum_of_time -= .60
        else:
            if int(str(sum_of_time)[2:4]) >= 60:
                sum_of_time += 1
                sum_of_time -= .60

        if sum_of_time > 12:
            if am_or_pm_time == "AM":
                print(sum_of_time)
                new_time = "{:.2f} PM".format(sum_of_time)
                new_time = new_time.replace('.',':',1)
            elif am_or_pm_time == "PM":
                new_time = "{:.2f} AM".format(sum_of_time)
                new_time = new_time.replace('.',':',1)
        else:
            if am_or_pm_time == "AM":
                new_time = "{:.2f} AM".format(sum_of_time)
                new_time = new_time.replace('.',':',1)
            elif am_or_pm_time == "PM":
                new_time = "{:.2f} PM".format(sum_of_time)
                new_time = new_time.replace('.',':',1)


    print(new_time)
    return new_time


add_time("11:40 AM", "0:25")
