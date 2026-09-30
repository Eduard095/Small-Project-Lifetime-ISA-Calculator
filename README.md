# Lifetime ISA Calculator

If you're saving for your first home, this calculator is for you!

This project estimates how much a Lifetime ISA (LISA) could be worth by the time you buy your first home. You enter two things:

1. How much you want to save each month
2. How many years until you plan to buy

It then calculates your estimated balance, including the 25% government bonus and interest.

> **Note:** This is an illustrative estimate only and monthly contributions only.

## How it works

The calculation logic is written in Python and exposed through a REST API built with FastAPI:

The API validates all input before any calculation runs. Contributions must be between £0 and £333.33 a month (the £4,000 annual LISA limit), and the savings period must be between 1 and 32 years. Invalid input is rejected with a clear error message explaining which field is wrong.

## Roadmap

- [x] Calculation logic and command-line version - Python
- [x] REST API with input validation - fastAPI
- [x] Automated API tests
- [x] React front end - TypeScript
- [ ] Save and compare savings scenarios (database)
- [ ] Docker setup
- [ ] Continuous integration with GitHub Actions
- [ ] Deploy online

<img width="1894" height="856" alt="image" src="https://github.com/user-attachments/assets/4b3f72ef-3a9d-401a-9604-afbd0eff1274" />