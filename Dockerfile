FROM python:3.11.9
WORKDIR D:\projects\orison_tech\student_performance
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["streamlit", "run", "main.py", "--server.port=5000"]