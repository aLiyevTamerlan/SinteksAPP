.PHONY: dev makemigrations migrate run stamp

stamp:
	@echo "🔖 Stamping current DB state..."
	@alembic stamp head
	@echo "✅ Database stamped!"

makemigrations:
	@echo "🔄 Generating new migrations..."
	@alembic revision --autogenerate -m "$(MSG)"
	@echo "✅ New migrations generated!"

migrate:
	@echo "🔄 Running Alembic migrations..."
	@alembic upgrade head
	@echo "✅ Database migrations applied!"

run: migrate
	@echo "🚀 Starting FastAPI..."
	@uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers=4

dev:
	@echo "🚀 Starting FastAPI..."
	@uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload --log-level info
