#!/bin/bash
sikuli_jar=sikuli-script.jar
robotframework_jar=robotframework-2.8.1.jar

/Library/Java/JavaVirtualMachines/1.6.0.jdk/Contents/Home/bin/java -cp sikuli-script.jar \
-Dpython.path="${robotframework_jar}\Lib":"${sikuli_jar}\Lib" \
org.robotframework.RobotFramework \
--pythonpath=content-studio.sikuli \
--outputdir=TestResults \
--noncritical non-critical \
--loglevel=TRACE \
$@

