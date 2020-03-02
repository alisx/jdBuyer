import threading
from spider import JDSpider, should_monitor, time
from config import configs
import queue as Queue
from log.jdlogger import logger
import sys

class Runner(threading.Thread):
    def __init__(self, threadId, spider, conf):
        threading.Thread.__init__(self)
        self.conf = conf
        self.spider = spider
        self.threadId = threadId
    def run(self):
        """
        TODO
        1 如果有预约时间，预约标记为需预约，先预约，预约成功后，改变标记为预约成功，
          预约失败后，预约标记为失败
          无预约时间，预约标记直接为预约成功
        2 只有预约标记为成功才进行购买
        """
        # TODO 
        print(self.conf.reserveFlag)
        if self.conf.reserveFlag == 'need':
            logger.info(f"{self.conf.good} 需要预约")
            if not should_monitor(self.conf.reserveTimer):
                logger.info(f"{self.conf.good} 预约时间未到 等待中")
            while True:
                if should_monitor(self.conf.reserveTimer):
                    logger.info(f"{self.conf.good} 可以预约了")
                    while not self.spider.reserve(self.conf.good) and self.conf.flush:
                        logger.info(f"{self.conf.good} 未约到，继续")
                        time.sleep(self.conf.wait / 1000.0)
                    logger.info(f"{self.conf.good} 预约成功！！！")
                    self.conf.reserveFlag = 'succ'
                    break
                time.sleep(1)
            logger.info(f"{self.conf.good} 结束预约过程\n")
        # if self.conf.reserveFlag == 'succ':
        #     while True:
        #         if should_monitor(self.conf.timer):
                    
        #             while not self.spider.buy(self.conf) and self.conf.flush:
        #                 time.sleep(self.conf.wait / 1000.0)
        #             break
        #         time.sleep(1)

# reserveQ = Queue.Queue(100)
# buyQ = Queue.Queue(100)

def init():
    threads = []
    id = 0
    spider = JDSpider()
    if not spider.checkLogin():
        if not spider.login_by_QR():
            sys.exit(-1)

    for c in configs:
        # if c.reserveFlag == 'need':
        #     reserveQ.put(c)
        # else:
        #     buyQ.put(c)
        threadId = c.good + "_" + str(id)
        thread = Runner(threadId=threadId, spider= spider, conf=c)
        thread.start()
        threads.append(thread)
        id += 1
    return threads


if __name__ == '__main__':
    threads = init()
    for t in threads:
        t.join()

