[Simple instructions](http://news.ycombinator.com/item?id=1054036):

    $ mkdir google-indexer && cd google-indexer
    $ wget http://bugs.jython.org/file756/google-indexer.zip
    $ unzip google-indexer.zip
    $ svn co https://jython.svn.sourceforge.net/svnroot/jython/trunk/jython
    $ cd jython
    $ patch -p0 < ../google-indexer-patch.diff
    $ tar zxvf ../google-indexer-newfiles.tar.gz
    $ ant jar

And then (following the suggestion in the top of the HtmlDemo class - see src/org/python/indexer/demos/HtmlDemo.java for how to do this on the whole stdlib)

    $ java -classpath ./dist/jython-dev.jar:./extlibs/antlr-runtime-3.1.3.jar:./extlibs/constantine.jar org.python.indexer.demos.HtmlDemo /usr/lib/python2.4/email

This will produce a set of files in html/. Use a suitable browser to view

    $ google-chrome html/Message.py.html

