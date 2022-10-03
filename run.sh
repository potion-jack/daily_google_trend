source commit_machine/bin/activate 2>/dev/null  || :

python __main__.py
python cleaner.py

git add .
git commit -m "in oracle  $(date)"
git push origin in_oracle
