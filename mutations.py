def mutate_string(s, p, character):
    s=s[:p] + s[p+1:]
    s=s[:p] + character + s[p:]
    #string[position]=character
    return s
    

if __name__ == '__main__':
