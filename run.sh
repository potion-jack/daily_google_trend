source commit_machine/Scripts/activate
python __main__.py
python cleaner.py
git add .
git commit -m "in oracle  $(date)"
git push origin main
