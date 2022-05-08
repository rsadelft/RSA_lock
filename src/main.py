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
p1 = PWM(Pin(15))
p1.freq(500)
p1.duty(0)
try:
    updater.update()
    p1.freq(500)
    p1.duty(512)
    time.sleep(2)
    p1.deinit()
except Exception as e:
    log('Failed to OTA update:', e)
    p1.freq(400)
    p1.duty(512)
    time.sleep(10)
    p1.deinit()


from src.lib.service import start
start()
