# Website Difference Detector

Detect differences from a website through time via git commits

## Technological Requirements : 
- git
- git bash
- python 3
- web browser for testing

## Detecting differences :
** Perform these actions in a git bash cli for most success
Here are the steps to perform a difference detection :

1. Produce the webDump to analyze and create the necessary files to process the webDump. This is done in the indexProducer.py file, so to generate the web dump and the necessary files, simply run : `py indexProducer.py`

2. Obtain the difference between this dump and the previous dump by running git diff : `git diff HEAD websiteDump.html > difflog.txt`

3. Find the differences you are looking for and store them in a place that will be used by your difference showing page. This is done in the findDifferences.py file. To execute it, do : `py findDifferences.py`

4. Run the difference showing page in a browser to see the result. In this case, we have `index.html` which can be opened by any browser.

5. If you are happy with the result, you can commit the changes, which will make your system prepared for the next change.

6. If you want to automate this process, you can put this all in one bash script and then call that bash script on a regular basis (like `runScript.sh` which can be run in the git bash cli with `./runScript.sh`).


