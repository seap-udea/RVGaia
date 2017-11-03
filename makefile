clean:
	@find . -name "*~" -exec rm {} \;
	@find . -name "#*#" -exec rm {} \;
	@find . -name "__*__" -exec rm -r {} \;

pull:
	@-git reset --hard HEAD
	@-git pull

commit:
	@echo "Commiting..."
	@-git commit -am "Commit"
	@-git push origin master
