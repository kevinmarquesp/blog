compile:
	$(eval BASENAME="$(shell basename ${FILE})")
	$(eval HTML="$(shell echo ${BASENAME} | cut -d. -f1).html")
	@pandoc -s ${FILE} -c none --template template/blog_post.html --toc --toc-depth=6 -o posts/${HTML}
	@make compileindex


compileindex:
	@cp template/index_template.md tmp.md
	@python gen_posts_list.py >> tmp.md
	@pandoc -s tmp.md -c none --template template/blog_post.html --toc --toc-depth=6 -o index.html
	@rm tmp.md
