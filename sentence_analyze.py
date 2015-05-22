#standard library
from string import strip
import urllib2

#user library
from vocab import verb,article
from data_url import word_type

def sen_ana(sentence):

    wtype=[];
    word=sentence.strip().split();
    print word;

    for w in word:
        
        print w+" : ";

        # Verb search
        try:
            v=verb.index(w.lower());
            print "v : "+str(verb.index(w.lower()));
        except ValueError:
            v=-1;
            print "not verb";

        # Article search
        try:
            a=article.index(w.lower());
            print "a : "+str(article.index(w.lower()));
        except ValueError:
            a=-1;
            print "not article"; 

        # Search in the dictionary
        wt=word_type(w);
        print wt[0];

        # Setup results
        if v!=-1:
            wtype.append('Verb');
        elif a!=-1:
            wtype.append('Article');
        elif wt[0]!='none':
            wtype.append(wt[0]);
        else:
            wtype.append('-');

        # Separate each word with newline 
        print "\n";

    # Get verb position
    vpos=wtype.index('Verb');

    # Predict sentence by the verb position
    sub=str(word[:(vpos)]);
    rel=str(word[vpos]);
    obj=str(word[(vpos+1):]);

    # Show results
    print wtype;
    print "s:"+sub+"\nr:"+rel+"\no:"+obj;
            
    return wtype
