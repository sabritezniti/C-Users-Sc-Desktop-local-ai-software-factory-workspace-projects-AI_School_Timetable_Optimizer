# AI School Timetable Optimizer

## Project Overview

This project aims to develop a smart application that automates the creation and organization of school timetables based on data provided in an Excel file. The application will handle various constraints and generate optimal timetables while ensuring all requirements are met.

## Install/Run Steps

### Prerequisites

1. **Python**: Ensure Python 3.8 or higher is installed on your system.
2. **Google OR-Tools**: Install the OR-Tools library using pip:
   ```bash
   pip install ortools
   ```
3. **Pandas**: Install the Pandas library for data manipulation:
   ```bash
   pip install pandas
   ```
4. **OpenPyXL**: Install the OpenPyXL library for reading and writing Excel files:
   ```bash
   pip install openpyxl
   ```
5. **ReportLab**: Install the ReportLab library for generating PDF reports:
   ```bash
   pip install reportlab
   ```
6. **SQLite**: Install the SQLite library for database operations:
   ```bash
   pip install sqlite3
   ```
7. **Streamlit**: Install the Streamlit library for the frontend:
   ```bash
   pip install streamlit
   ```

### Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/ai-school-timetable-optimizer.git
   cd ai-school-timetable-optimizer
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. Start the Streamlit server:
   ```bash
   streamlit run main.py
   ```

2. Open your web browser and navigate to `http://localhost:8501` to access the application.

## Project Structure

```
/app
/ui
/optimizer
/models
/excel
/validation
/reports
/database
main.py
requirements.txt
README.md
```

## Next Steps

1. **Excel Template**: Create a sample Excel template for data input.
2. **Data Validation Engine**: Implement the data validation engine to check for errors in the input data.
3. **Optimization Engine**: Develop the optimization engine using Google OR-Tools.
4. **Timetable Generator**: Create the timetable generator based on the validated data.
5. **Scoring System**: Implement the scoring system to evaluate the quality of the generated timetables.
6. **Dashboard**: Design and implement the user interface dashboard.
7. **Manual Editing**: Allow users to manually edit the timetable and re-optimize.
8. **Export Excel**: Implement functionality to export the timetable to Excel.
9. **Export PDF**: Implement functionality to export the timetable to PDF.
10. **AI Explanation Assistant**: Add an AI assistant to explain the optimization process and suggest improvements.

By following these steps, you will have a fully functional AI school timetable optimizer application.