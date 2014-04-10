@echo off
 
set sikuli_jar=C:\Program Files\Sikuli X\sikuli-script.jar
set robotframework_jar=C:\Test-automation\ContentStudio\robotframework-2.8.1.jar
 
java -cp "robotframework-2.8.1.jar;%sikuli_jar%" ^
-Dpython.path="%robotframework_jar%\Lib";"%sikuli_jar%\Lib" ^
org.robotframework.RobotFramework ^
--pythonpath=content-studio.sikuli ^
--outputdir=TestResults ^
--loglevel=TRACE ^
%*