init:
	python3 -m venv .venv && \
	source .venv/bin/activate && \
	python3 -m pip install -r requirements.txt && \
	mkdocs new .

serve:
	source .venv/bin/activate && \
	pgrep ython | xargs kill && \
	(nohup python3 ./secrets/app.py 2>&1 &) && \
	python3 -m mkdocs serve
