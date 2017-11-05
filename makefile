clean:
	@find . -name "*~" -exec rm {} \;
	@find . -name "#*#" -exec rm {} \;
	@find . -name "*.pyc" -exec rm -r {} \;
	@rm -rf __*__

pull:
	@-git reset --hard HEAD
	@-git pull

commit:
	@echo "Commiting..."
	@-git commit -am "Commit"
	@-git push origin master

purge:
	@rm -r Store/*--*
pack:
	@bash Store/store.sh pack
unpack:
	@bash Store/store.sh unpack
