from datetime import date


def format_time_interval(seconds):
    return '{}:{}'.format(abs(seconds) // 60, str(abs(seconds) % 60).zfill(2))


def write_info(filename, dt, itype, description):
    with open(filename, 'a') as f:
        formatted_time = format_time_interval(int(dt.total_seconds()))
        today = date.today()
        f.write('{},{},{},{}\n'
                .format(today.isoformat(), formatted_time, itype, description))
