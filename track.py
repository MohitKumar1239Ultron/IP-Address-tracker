import pygeoip
gip = pygeoip.GeoIP("GeoLiteCity.dat")
res = gip.record_by_addr('23.235.60.92')
for key, val in res.items():
    print('%s : %s' % (key,val))
