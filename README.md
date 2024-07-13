Install and open Visual Studio Code - https://code.visualstudio.com/Download

Clone repository
    - View -> Source Control -> Clone Repository -> https://github.com/nicktownsend88/fetch.git

Install Python 3.8 or higher - https://www.python.org/downloads/
    - Make sure to add python to the PATH

Install Playwright for Python - https://playwright.dev/python/docs/intro
    - Execute the following commands:
        pip install pytest-playwright
        python3 -m playwright install

Running the test:
    - Open Terminal in Visual Studio Code
    - Execute the following command: pytest test_fetch.py --headed --verbose -s
    (this command may be needed for Windows:  python3 -m pytest test_fetch.py --headed --verbose -s
    
