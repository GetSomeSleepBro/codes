# Expert System Programs

This workspace contains six simple expert-system programs. Each program has its own folder with:

- `frontend/` - a small HTML, CSS, and JavaScript user interface.
- `backend/` - a Python backend with rule-based expert-system logic.
- `report/` - a short report you can expand for submission.

## How To Run Any Program

1. Open a terminal in the selected program folder.
2. Run the backend:

```bash
python3 backend/server.py
```

3. Open the local URL shown in the terminal, usually:

```text
http://localhost:8000
```

4. Fill the form and click the decision button.

## Folder List

- `01_information_management`
- `02_hospital_medical_facilities`
- `03_help_desk_management`
- `04_employee_performance_evaluation`
- `05_stock_market_trading`
- `06_airline_cargo_scheduling`

## Notes

- The systems are intentionally simple and easy to explain.
- The backend uses `http.server`, so no Flask/Django setup is required.
- The expert-system rules are written as normal `if/elif` statements with comments.
- You can submit any one folder if your assignment asks for only one expert system.

