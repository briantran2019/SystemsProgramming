import command_runner, os

#set working directory to current directory of script at runtime
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

cmd = command_runner.CommandRunner()

cmd.run_command("ls -l")

cmd.parse_ls_output()
