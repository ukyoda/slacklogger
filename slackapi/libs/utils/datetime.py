from datetime import datetime, timedelta, timezone
JST = timezone(timedelta(hours=+9), 'Asia/Tokyo')

def now():
    return datetime.now(JST)

def today_start():
    dt = now()
    return get_start_dt(dt)

def yesterday_start():
    dt = now() - timedelta(days=1)
    return get_start_dt(dt)

def tomorrow_start():
    dt = now() + timedelta(days=1)
    return get_start_dt(dt)

def get_start_dt(target_dt):
    return datetime(target_dt.year, target_dt.month, target_dt.day)

def from_timestamp(timestamp):
    return datetime.fromtimestamp(timestamp, JST)