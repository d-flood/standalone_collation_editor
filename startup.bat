SET BASEDIR="%CD%"
echo %BASEDIR%

start java -jar collatex/collatex-tools-1.8-SNAPSHOT.jar -S
python3 bottle_server.py %BASEDIR%
