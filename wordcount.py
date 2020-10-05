# put your code here.

def count_words(filename):
    
    text = open(filename)
    all_words = []

    for line in text:
        line = line.rstrip()
        words = line.split(" ")
        print("words: ", words)
        
        
    print("ALL WORDS: ", all_words)
