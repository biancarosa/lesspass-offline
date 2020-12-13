install:
	cd lesspass/packages/lesspass-pure && yarn install

build:
	cd lesspass/packages/lesspass-pure && yarn build

deploy:
	firebase deploy

zip:
	cd lesspass/packages/lesspass-pure/dist && zip -r lesspass-offline.zip *
	cd -
	mv lesspass/packages/lesspass-pure/dist/lesspass-offline.zip .
	