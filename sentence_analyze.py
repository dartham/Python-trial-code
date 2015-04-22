from string import strip

def sen_ana(sentence):
    
    verb=['be','is','am','are','run','eat','walk'];
    
    word=sentence.strip().split();
    print word;
    
    for r in verb:
        try: print word.index(r);
        except ValueError: print "-1";
        
    #print "s:"+sub+"\nr:"+rel+"\no:"+obj;
        
    return
