languages = ['python', 'perl', 'c', 'java']

for lang in languages:
    if lang in ['python', 'perl']:
        print("%6s need interperter" % lang)
    elif lang in ['c', 'java']:
        print("%6s need complier" % lang)
    else:
        print("should not reach here")
        