# Responsive-Component-Detector
Responsive component Detector is a tool that detects the responsive feature of website or desktop and returns the cordinate values of the same.

##Approach

Features are detected using canny edge detector algorithm.
Features are marked using closed loop contour on the basis of approximate arc length
Area detected by contour help increase in the intensity value at that pixels.
Those pixel values can be retained and remainder part can be transformed into binary values.
Which gives flexibility to extract the cordinate.
For finding target feature clustring algorithm can be used by eliminating all the untargeted feature 
After applying clustering image we will have the image containing only target feature .
Then extracting row and column value can be achived at greater accuracy which forms the cordinate points of each feature.
Extracted feature file will be stored in a JSON format

## Things Done
Detecting feature of rounded shape

## Things to be done
Detecting different shaped feature
Applying Cluster algorithm
Extracting Cordinate and converting to JSON format

###Note
*Approach may change for tools adaptation towards generality*
