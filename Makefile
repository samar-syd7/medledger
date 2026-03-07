install:
	pip install -r requirements.txt

run:
	uvicorn api.main:app --reload

node:
	cd blockchain && npx hardhat node

deploy:
	cd blockchain && npx hardhat ignition deploy ./ignition/modules/Lock.js --network localhost
