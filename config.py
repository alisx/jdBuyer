config = [{
    'good': '65624145328',
    'reserveTimer': '11:00:00',
    'timer': ''
}, {
    'good': '100011551632',
    'reserveTimer': '15:00:00',
    'timer': '19:59:55'
}, {
    'good': '100011521400',
    'reserveTimer': '21:00:00',
    'timer': '09:59:55'
}, {
    'good': '100011345090',
    'reserveTimer': '21:00:00',
    'timer': '09:59:55'
}]

# config = [{
#     'good': '65624145328',
#     'reserveTimer': '11:00:00',
#     'timer': ''
# }]
class Conf:
    def __init__(self, area='1_2808_51531_0', good='100005171461',
                 count=1, wait=1000, flush=True, submit=False, reserveTimer='', timer=''):
        self.area = area
        self.good = good
        self.count = count
        self.wait = wait
        self.flush = flush
        self.submit = submit
        self.timer = timer
        self.reserveTimer = reserveTimer
        self.reserveFlag = 'succ' # succ need fail
        if self.reserveTimer:
            self.reserveFlag = 'need' # succ need fail


configs = []
for c in config:
    configs.append(Conf(
        area=c.get('area', None),
        good=c.get('good', None),
        count=c.get('count', None),
        wait=c.get('wait', None),
        flush=c.get('flush', None),
        submit=c.get('submit', None),
        reserveTimer=c.get('reserveTimer', None),
        timer=c.get('timer', None)
    ))
