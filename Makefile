install:
	cd lesspass/packages/lesspass-pure && yarn install

build:
	cd lesspass/packages/lesspass-pure && yarn build

deploy:
	firebase deploy
	
zip:
	tar -czf lesspass-offline.tar.gz lesspass/packages/lesspass-pure/dist