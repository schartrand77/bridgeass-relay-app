# Use a lightweight base image
FROM python:3.10-slim as builder

# Install dependencies
RUN pip install fastapi uvicorn requests

# Create a directory for the app
WORKDIR /app

# Copy the app code
COPY . .

# Use a production-ready image for the final build
FROM python:3.10-slim

# Install only the necessary runtime dependencies
RUN pip install fastapi uvicorn requests

# Copy the app code from the builder stage
WORKDIR /app
COPY --from=builder /app /app

# Expose the port the app will run on
EXPOSE 8000

# Run the app
CMD ["uvicorn", "relay_app:app", "--host", "0.0.0.0", "--port", "8000"]