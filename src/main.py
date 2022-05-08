import update, env, lib.requests, lib.logger, lib.requests, lib.timew, time, os, machine
from lib import base64
from machine import Pin, PWM

t = lib.timew.Time(time=time)

# Configure Logger
logger = lib.logger.config(enabled=True, include=env.settings['logInclude'], exclude=env.settings['logExclude'],
                           time=t)
log = logger(append='boot')
log("The current time is %s" % t.human())

loggerOta = logger(append='OTAUpdater')

io = update.IO(os=os, logger=loggerOta)
github = update.GitHub(
    io=io,
    remote=env.settings['githubRemote'],
    branch=env.settings['githubRemoteBranch'],
    logger=loggerOta,
    requests=lib.requests,
    username=env.settings['githubUsername'],
    token=env.settings['githubToken'],
    base64=base64,
)
updater = update.OTAUpdater(io=io, github=github, logger=loggerOta, machine=machine)

try:
    updater.update()
    p1 = PWM(Pin(15))
    p1.freq(500)
    p1.duty(512)
    time.sleep(1)
    p1.deinit()
    time.sleep(2)
except Exception as e:
    log('Failed to OTA update:', e)
    p1 = PWM(Pin(15))
    p1.freq(500)
    p1.duty(512)
    for _ in range(3):
        p1.duty(0)
        time.sleep(0.5)
        p1.duty(512)
        time.sleep(1)
    p1.deinit()
    time.sleep(2)



from src.lib.service import start
start()
