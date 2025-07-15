import datetime

x = datetime.datetime.now()
print(x)
print(x.strftime("%A"))
print(x.strftime("%a"))
print(x.year)

# %Y	Jahr, vierstellig	2025
# %y	Jahr, zweistellig	25
# %m	Monat (01–12)	07
# %B	Monat (Name, lang)	July
# %b	Monat (Name, kurz)	Jul
# %d	Tag im Monat (01–31)	08
# %A	Wochentag (Name, lang)	Tuesday
# %a	Wochentag (Name, kurz)	Tue
# %w	Wochentag (0 = Sonntag)	2
# %j	Tag im Jahr (001–366)	189

# ⏰ Uhrzeit-Formatierungen
# Code	Bedeutung	Beispiel
# %H	Stunde (00–23, 24h)	16
# %I	Stunde (01–12, 12h)	04
# %p	AM / PM	PM
# %M	Minute (00–59)	47
# %S	Sekunde (00–59)	09
# %f	Mikrosekunden (000000–999999)	123456

# 🌍 Zeitzone und Sonstiges
# Code	Bedeutung	Beispiel
# %z	UTC-Offset	+0200
# %Z	Zeitzonenname	CEST
# %c	Lokales Datum & Uhrzeit	Tue Jul 8 16:47:00 2025
# %x	Lokales Datum	07/08/25
# %X	Lokale Uhrzeit	16:47:00

# # %%	Prozentzeichen %	%
# ISO-Format	%Y-%m-%d %H:%M	2025-07-08 16:47
# Deutsch, lesbar	%d.%m.%Y %H:%M	08.07.2025 16:47
# Nur Uhrzeit	%H:%M:%S	16:47:00
# Für Dateinamen	%Y%m%d_%H%M%S	20250708_164700