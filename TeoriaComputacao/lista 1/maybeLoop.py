def maybeLoop(inString):
    if not 'secret sauce' in inString:
        # enter an infinite loop
        i=0
        while i>=0:
            i=i+1
    else:
        # output “yes” if input length is even and “no” otherwise
        if len(inString) % 2 == 0:
            return 'yes'
        else:
            return 'no'