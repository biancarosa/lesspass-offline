install:
	cd lesspass/packages/lesspass-pure && yarn install

build:
	cd lesspass/packages/lesspass-pure && yarn build

deploy:
	firebase deploy

zip:
	cd lesspass/packages/lesspass-pure/dist && tar -czf lesspass-offline.tar.gz * && zip -r lesspass-offline.zip *
	cd -
	mv lesspass/packages/lesspass-pure/dist/lesspass-offline.tar.gz .
	mv lesspass/packages/lesspass-pure/dist/lesspass-offline.zip .
	