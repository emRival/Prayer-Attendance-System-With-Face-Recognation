FROM python:3.10.15

# Set the working directory
WORKDIR /usr/app

# Copy the current directory contents into the container at /app/absen
COPY . .

# Install CMake, libGL, dan dependencies lainnya
RUN apt-get update && apt-get install -y cmake libgl1

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set entrypoint to allow file choice
ENTRYPOINT ["python"]
