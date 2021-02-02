 #!/bin/bash
 
 
 
 curl -X POST -H "Content-Type: text/plain" --trace-ascii debugdump.txt --data-binary @"To Thee Old Cause
.txt" http://127.0.0.1:5000/upload/old_cause.txt 
#curl -X POST --data-binary @Hamlet.txt http://127.0.0.1:5000/upload/Hamlet.txt
#curl -X POST --data @Hamlet.txt http://127.0.0.1:5000/upload/Hamlet.txt




curl -X GET  http://0.0.0.0:5000/word_vocab