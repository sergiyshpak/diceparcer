

curl -v --silent "https://www.dice.com/jobs?l=FL&sort=date&p=1" --stderr - | grep jobLoc >FL.txt
curl -v --silent "https://www.dice.com/jobs?l=FL&sort=date&p=2" --stderr - | grep jobLoc >>FL.txt
curl -v --silent "https://www.dice.com/jobs?l=FL&sort=date&p=3" --stderr - | grep jobLoc >>FL.txt
curl -v --silent "https://www.dice.com/jobs?l=FL&sort=date&p=4" --stderr - | grep jobLoc >>FL.txt
curl -v --silent "https://www.dice.com/jobs?l=FL&sort=date&p=5" --stderr - | grep jobLoc >>FL.txt


