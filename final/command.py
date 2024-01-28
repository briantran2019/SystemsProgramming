from subprocess import Popen as popen, PIPE


class Command:
    @staticmethod
    def run_command_method(cmd: bytes) -> bytes:
        # TODO: Implement the method using subprocess.Popen
        # the popen command might need type str not bytes
        cmdarr = cmd.decode().split()
        runcmd = popen(cmdarr, stdout = PIPE, stderr = PIPE, text=True)
        cmdout, cmderr = runcmd.communicate()
        if runcmd.returncode != 0:
            return cmderr.encode()
        return cmdout.encode()