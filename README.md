
## Schema Design

![diagram-export-16-11-2024-10_46_52](https://github.com/user-attachments/assets/c9f34ae0-00b6-4510-ba1a-8ca1d807acc1)

# Technical Design
## 1. Introduction
- **Purpose**
- **Scope**
- **Definitions, Acronyms, and Abbreviations**
## 2. System Overview
- **High-Level Architecture**
- **Key Components**
## 3. API Design and Implementation
- **Overview**
- **Endpoints**
    - **Customers**
        - GET all Customers (API), Search enabled
        - Create new Customers (API)
        - Delete or Update Customer details (CMS)
    - **Products**
        - GET all Products (API)
        - POST new Products (CMS)
        - Delete or Update Product details (CMS)
    - **Credit Transactions**
        - Get all Transactions (API), Search and Filter
        - Create new Transactions (API)
        - Update/Delete Transactions (CMS)
    - **Receivables**
        - Get all Receivables (API), Search and Filter
        - Create a Receivable (API)
        - Update/Delete Receivables (CMS)
        - Get Current Credit MV (API)
    - **Machines**
        - Create new DU machines (CMS)
        - Delete/Update DU machines (CMS)
        - List all machines (API), Filter by Product code
    - **DailyDUSales**
        - Write new Readings for Machines (API)
        - Update/Delete Readings (CMS)
        - List all readings, filter and search
    - **LubeInventory**
        - Create/Update/Delete (CMS)
    - **DailyLubeSales**
        - Create/Update/Delete Sale record (CMS)
        - Get all daily sales records, filter and search
        - Get current live stock with Value (API)
    - **Accounts**
        - Create/Update/Delete Accounts (CMS)
        - List all Accounts available (API)
    - **Transaction Type**
        - Create/Update/Delete Transaction Type (CMS)
        - List all Transaction type (API)
    - **Transactions**
        - Create Transactions (API)
        - Get all Transactions, filter and search
        - Update/Delete Transactions (CMS)
## 4. Asynchronous Tasks
- **Components Used**
    - Celery
    - RabbitMQ
## 5. Security Considerations
- **Authentication and Authorization**
- **API Rate Limiting**
- **Secure Data Storage**
## 6. Testing Strategy
- **Unit Testing**
- **Integration Testing**
- **End-to-End Testing**
- **Load Testing**
## 7. Performance Metrics
- **Response Time**
- **Throughput**
- **Scalability**
- **Resource Utilization**
## 8. Error Logging and Monitoring
- **Centralized Logging System**
- **Real-Time Monitoring Tools**
- **Automated Alerts and Notifications**
## 9. Deployment Strategy
- **Continuous Integration/Continuous Deployment (CI/CD)**
- **Containerization with Docker**
- **Cloud-Based Deployment**
## 10. Maintenance and Support
- **Guidelines for Maintenance**
- **Support Resources**
## 11. Appendices
- **Glossary**
- **References**
1. Customers
    1. GET all Customers (API), Search enabled
    2. Create new Customers (API)
    3. Delete or Update Customer details (CMS)
2. Products
    1. GET all Products (API)
    2. POST new Products (CMS)
    3. Delete or Update Product details (CMS)
3. Credit Transactions
    1. Get all Transactions (API), Search for Customer name, Product code. Filter by Product code, Date range of purchase. Ordering for Total price, Customer name etc
    2. Create new Transactions (API)
    3. Update/Delete Transactions (CMS)
4. Receivables
    1. Get all Receivables (API), Search for Customer name, Filter by Date range of purchase. Ordering for Amount received, Customer name etc
    2. Create a Receivable (API)
    3. Update/Delete Receivables (CMS)
    4. Get Current Credit MV (API)
5. Machines
    1. Create new DU machines (CMS)
    2. Delete/Update DU machines (CMS)
    3. List all machines (API), Filter by Product code
6. DailyDUSales
    1. Write new Readings for Machines (API)
    2. Update new Readings for Machines, one reading per machine in a day. (API)
    3. Delete Readings (CMS)
    4. List all readings, filter by machine code, Product code, date range
7. LubeInventory
    1. Create/Update/Delete (CMS)
8. DailyLubeSales
    1. Create Sale record (API)
    2. Update/Delete Sale record (CMS)
    3. Get all daily sales records, filter by Product code, search by Product code, Ordering for required fields (API)
    4. Get current live stock with Value (API) from Current Live Stock MV
9. Accounts
    1. Create/Update/Delete Accounts (CMS)
    2. List all Accounts available (API)
10. Transaction Type
    1. Create/Update/Delete Transaction Type (CMS)
    2. List all Transaction type (API)
11. Transactions
    1. Create Transactions (API)
    2. Get all Transactions filter by Transaction type, Account type, date range, Search Transaction type, Account type (API)
    3. Update/Delete Transactions (CMS)



