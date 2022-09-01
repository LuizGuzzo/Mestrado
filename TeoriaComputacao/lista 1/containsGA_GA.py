def containsGA_GA(s):
    index = s.find("GAG")
    if index > 0:
        if s[index+3] == "A":
            return 'yes'

    return 'no'