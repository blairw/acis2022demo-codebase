OUTPUT_FILE="./outputs/02-coding/report.html"

source .venv/bin/activate

cat ./coding/*.yml > ./AllCodes.yml

python3 scripts/match_coding.py

echo > $OUTPUT_FILE
cat ./templates/html/010-header-part1.html >> $OUTPUT_FILE

echo "<script>" >> $OUTPUT_FILE
cat ./templates/js/node_modules/jquery/dist/jquery.min.js >> $OUTPUT_FILE
echo "</script>" >> $OUTPUT_FILE

cat ./templates/html/010-header-part2.html >> $OUTPUT_FILE
echo "<h1>Quotes and Open Codes</h1>" >> $OUTPUT_FILE
cat ./outputs/02-coding/df_quotes.html >> $OUTPUT_FILE
echo "<h1>Axial Codes</h1>" >> $OUTPUT_FILE
cat ./outputs/02-coding/df_all_codes.html >> $OUTPUT_FILE
cat ./templates/html/090-footer.html >> $OUTPUT_FILE

# Done
deactivate
echo "Done"
