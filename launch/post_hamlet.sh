 #!/bin/bash
 
 
 
 curl -X POST -H "Content-Type: text/plain" --trace-ascii debugdump.txt --data-binary @"Hamlet.txt" http://127.0.0.1:5000/upload/Hamlet.txt 
#curl -X POST --data-binary @Hamlet.txt http://127.0.0.1:5000/upload/Hamlet.txt
#curl -X POST --data @Hamlet.txt http://127.0.0.1:5000/upload/Hamlet.txt