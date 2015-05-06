@echo off
 
set sikuli_jar=sikuli-script.jar
set robotframework_jar=C:\Test-automation\ContentStudio\robotframework-2.8.1.jar
 
jre6\bin\java -cp "robotframework-2.8.1.jar;%sikuli_jar%" ^
-Dpython.path="%robotframework_jar%\Lib";"%sikuli_jar%\Lib" ^
org.robotframework.RobotFramework ^
--pythonpath=content-studio.sikuli ^
--outputdir=TestResults ^
--noncritical non-critical ^
--loglevel=TRACE ^
%*

xcopy %tmp%\hs_err_pid*.log TestResults\Logs
xcopy %tmp%\com.escenic.studio\log\*.log TestResults\Logs
