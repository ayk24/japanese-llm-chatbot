run:
	poetry run streamlit run app.py

lint:
	poetry run isort .
	poetry run black .