NamasteKart-Order-Validation-System
-------------------------------------------

An automated data validation and file processing project built to ensure daily retail orders are accurate, clean, and business-ready.
This project focuses on validating transactions for NamasteKart (operating in Bangalore and Mumbai) using Python with robust error handling and file segregation.

Tech Stack
-----------------

Python (csv, os, datetime, shutil) – File processing, validations, and automation

CSV – Input order data & master product data

File System – Organized folder hierarchy for incoming, success, and rejected files

Data Source
------------------
- Product Master (product_master.csv)
  - Product ID
  - Price
  - Product Name
  - category
- Daily Orders (orders_YYYYMMDD.csv)
  - Order ID
  - Order Date
  - Product ID
  - Quantity
  - Sales Amount
  - City

Goal of the Project
----------------------------
Validate daily orders against strict business rules.

Move clean files to success_files and problematic files to rejected_files.

Generate error files listing rejected orders with detailed rejection reasons.

Ensure business users are quickly notified of data quality issues.

Validations Implemented
------------------------------------

Product Validation – Product ID must exist in product master.

Sales Validation – Sales amount must equal price × quantity.

Date Validation – Order date cannot be in the future.

Empty Field Validation – No missing values in order record.

City Validation – Orders must belong to Mumbai or Bangalore only.

Walkthrough of File Processing
-------------------------------------

Incoming Files → Stored in incoming_files/YYYYMMDD/.

Validation Checks → Each order record is validated.

Successful Files → If all orders in a file are valid, move file to success_files/YYYYMMDD/.

Rejected Files → If even one order fails, move full file to rejected_files/YYYYMMDD/.

Generate an additional file error_{filename}.csv with only rejected rows + rejection reasons.

Example Outcomes
------------------------

10 Incoming Files

8 Successful Files → All orders passed validations

2 Rejected Files → With corresponding error logs


Key Insights
--------------------------

Data Quality Assurance – Prevents bad data from reaching business dashboards.

Automation First – Hands-free daily execution with clear segregation of valid/invalid data.

Error Transparency – Provides detailed rejection logs for quick root cause analysis.

Scalable Framework – Can be extended with new validations, DB integration, or email alerts.


