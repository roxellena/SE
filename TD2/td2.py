import thrading,time,random
try:
    import Queue
    except:
        import queue as Queue

        class Producer:
            def __init__(self,sexe):
                self.genre=sexe.upper()
                self.nextTime=0

            def __repr__ (self):
                if self.genre=='M':
                    return 'bonjour M'
                else:
                    return ' bonjour madame'
                
                def run(self):
                    global q
                    while(time.clock()<10):
                        if(self.nextTime<time.clock()):
                            f=self.sexe[random.randrange(len(self.sexe))]
                            q.put(f)


        class Consumer:
            def __init__(self):
                self.nextTime=0
                def run(self):
                    global q
                    while (time.clock()<10):
                        if(self.nextTime<time.clock() and not q.empty()):
                    f=q.get()
                    print("removing" +f)
                    self.nextTime += random.random()*2

    if __name__ == '__main__':
        q=Queue.Queue(10)

        p=Producer()
        c=Consumer()
        pt=threading.Thread(target=p.run,args=())
        ct=threading.Thread(target=c.run,args=())
        pt.start()
        ct.start()
