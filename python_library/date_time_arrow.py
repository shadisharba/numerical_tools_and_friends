import arrow

arrow.get('2013-05-11T21:23:58.970460+07:00')
utc = arrow.utcnow()
print(utc)  # Coordinated Universal Time (UTC)
print(utc.shift(hours=+1))
print(utc.to('Europe/Berlin'))
print(arrow.now())  # Local time

print(utc.timestamp())
print(utc.format())
print(utc.format('YYYY-MM-DD HH:mm:ss ZZ'))
print(utc.humanize())
print(utc.humanize(locale='DE'))