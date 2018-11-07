from CashInterpreter import interpret_command, get_cwd, startup

startup()
while True:
    command = raw_input(get_cwd() + " $ ")
    output = interpret_command(command)
    if output != []:
        print '\n'.join(output)
