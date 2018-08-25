import logging
import subprocess

LOG = logging.getLogger(__name__)
ADB_PATH = 'tools\\adb.exe'


def c(cmd):
    LOG.info('EXECUTING CMD: %s', cmd)
    subprocess.check_call(cmd)


def send_sms(msg, phone_number):
    LOG.info('SENDING TO %s: %s', phone_number, msg)
    c('{adb_path} shell am start -a android.intent.action.SENDTO '
      '-d sms:{phone_number} '
      '--es sms_body "{msg}" '
      '--ez exit_on_sent true'.format(adb_path=ADB_PATH,
                                      phone_number=phone_number,
                                      msg=msg))
    c('{adb_path} shell input keyevent 22'.format(adb_path=ADB_PATH))
    c('{adb_path} shell input keyevent 66'.format(adb_path=ADB_PATH))
