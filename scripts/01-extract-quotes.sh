source .venv/bin/activate

cd ../fulltexts

find . -type f -name "*.pdf" -exec python3 ../pdfannots/pdfannots.py {} -f json -o {}.json \;
mv *.json ../acis2022demo-codebase/outputs/01-extracted-quotes/

cd -

python3 scripts/unify_quotes.py

mv ./outputs/01-extracted-quotes/unified_quotes.html ./outputs/01-extracted-quotes/unified_quotes_OLD.html
echo > ./outputs/01-extracted-quotes/unified_quotes.html
cat ./templates/html/010-header-part1.html >> ./outputs/01-extracted-quotes/unified_quotes.html
cat ./templates/html/010-header-part2.html >> ./outputs/01-extracted-quotes/unified_quotes.html
cat ./outputs/01-extracted-quotes/unified_quotes_OLD.html >> ./outputs/01-extracted-quotes/unified_quotes.html
cat ./templates/html/090-footer.html >> ./outputs/01-extracted-quotes/unified_quotes.html
rm ./outputs/01-extracted-quotes/unified_quotes_OLD.html

# Done
deactivate
echo "Done"
