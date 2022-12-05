source .venv/bin/activate

cat ./coding/*.yml > ./AllCodes.yml

python3 scripts/match_coding.py

# Done
deactivate
echo "Done"
