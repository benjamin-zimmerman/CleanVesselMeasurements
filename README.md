# CleanVesselMeasurements
Cleans text files from Fiji of vessel measurements for further analysis


The software works with output from Fiji (ImageJ) measurements. 

For measuring the vessel lumen, it is useful to set up keyboard macros that make the measurement more comfortable. 

After downloading Fiji, open up the macros folder, and edit the "StartupMacros.fiji.ijm" file. 

You can change the keys that you use to measure, move forward, and move backward using this template:

macro "Measure with f9 [f9]" {
  run("Measure");
}

macro "Move forward with 0 [0]" {
  run("Next Slice [>]");
}

macro "Move backward with 9 [9]" {
  run("Previous Slice [<]");
}

Just append to the bottom of the text file and save.


In Fiji, you will want to change some settings before measuring.

In order to save out the slice position in Fiji, you must go to Analyze/Set Measurements, and check the Area and Stack Position options.
For some reason the Area has to be checked, even though you don't need it (and this script gets rid of it in the resultant measurements).

It is also useful to go to Analyze/Set Scale to map pixel distance to real units of length. If you do not know the conversion, you will need to measure it on the scope that you use to capture your image.

Use the line tool to draw a line between the two points that you wish to measure.

I recommend saving an ROI so that you can find where you drew your line (Analyze/Tools/ROI Manager/save), or just press "t" which is the shortcut.

After making the measurements, save the results. You can run the python code and select the results text file, and it will generate a new "clean" file with the suffix "_clean" appended to your results file name.
