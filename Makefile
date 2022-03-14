all: template.html index.template papers.template 
	./templify.py index papers
