py indexProducer.py
wait
git diff HEAD websiteDump.html > difflog.txt
wait
py findDifferences.py
wait
today=`date +%Y-%m-%d`
git add .
wait
git commit -m "Update "$today
wait
git push