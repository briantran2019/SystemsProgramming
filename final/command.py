from subprocess import Popen as popen, PIPE


class Command:
    @staticmethod
    def run_command(cmd: bytes) -> bytes:
        # TODO: Implement the method using subprocess.Popen
        # the popen command might need type str not bytes
        print(f'Executing command "{cmd}"')
        cmdarr = cmd.decode().split()
        runcmd = popen(cmdarr, stdout=PIPE, stderr = PIPE, text=True)
        cmdout, cmderr = runcmd.communicate()
        if runcmd.returncode != 0:
            print(f"Error: {cmderr}")
        else:
            print(f'Out: {cmdout}')
        return cmdout.encode()